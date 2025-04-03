"""Diagnostic script to plot ENSO metrics lifecycle."""

import logging
import os
from pprint import pformat

import iris
import matplotlib.pyplot as plt
import numpy as np
from esmvalcore.preprocessor import (
    extract_month,
)


from esmvaltool.diag_scripts.shared import (
    get_diagnostic_filename,
    group_metadata,
    run_diagnostic,
    save_figure,
    select_metadata,
)

# stdout
logger = logging.getLogger(os.path.basename(__file__))


def plot_level1(model_data, obs, metric_values, labels_ls):
    """Plot ENSO metric data, input data is model and obs."""
    figure = plt.figure(figsize=(10, 6), dpi=300)
    modls = [d[0] for d in metric_values]
    if labels_ls[1] in ['ENSO lifecycle']:
        # model first :list
        for datamod, name in zip(model_data[1], modls):
            plt.plot(model_data[0], datamod, label=name)
        plt.plot(*obs, label=f'ref: {labels_ls[2]}', linestyle='dashdot',
                 linewidth=3, color='black')

    plt.title(labels_ls[1])  # metric name
    plt.grid(linestyle='--')
    plt.ylabel(labels_ls[0])

    if labels_ls[1] == 'ENSO lifecycle':
        plt.legend(loc='center left', bbox_to_anchor=(0.98, 0.5))
        plt.axhline(y=0, color='black', linewidth=2)
        xticks = np.arange(1, 73, 6) - 36  # Adjust for lead/lag months
        xtick_labels = ['Jan', 'Jul'] * (len(xticks) // 2)
        plt.xticks(xticks, xtick_labels)
        plt.yticks(np.arange(-2, 2.5, step=1))
    plt.tight_layout()
    return figure


def sst_regressed(n34_cube):
    """Regression function for sst_time_series on sst_enso."""
    n34_dec = extract_month(n34_cube, 12)
    n34_dec_years = [n34_dec.coord('time').units.num2date(time).year
                     for time in n34_dec.coord('time').points]
    event_years = n34_dec_years[3:-3]  # leadlagyr
    # Ensure that the selected years are not the last years
    years_epochs = []
    for year in event_years:
        years_epochs.append([year - 2, year - 1, year,
                             year + 1, year + 2, year + 3])

    n34_selected = []
    for enso_epoch in years_epochs:
        # Select the data for the current year and append it to n34_selected
        year_enso = iris.Constraint(time=lambda cell: cell.point.year in
                                    enso_epoch)
        cube_2 = n34_cube.extract(year_enso)
        n34_selected.append(cube_2.data.data)

    event_constr = iris.Constraint(time=lambda cell: cell.point.year in
                                   event_years)
    n34_dec_ct = n34_dec.extract(event_constr)

    # 1) linear regression of sst_time_series on sst_enso
    a_data = np.array(n34_selected)
    b_data = n34_dec_ct.data
    b_with_intercept = np.vstack([b_data, np.ones_like(b_data)]).T
    coefs, _, _, _ = np.linalg.lstsq(b_with_intercept, a_data, rcond=None)

    return coefs[0]


def compute_enso_metrics(input_pair, dt_ls, var_group, metric):
    """Compute the ENSO metric for the collected preprocessed data."""
    fig = None
    metric_values = []
    model_plot = []
    # input_pair: obs first
    if metric == 'lifecycle':
        obs = sst_regressed(input_pair[0][var_group[0]])
        # model list, calc values
        for dataset in input_pair[1]:
            logger.info("%s, preprocessed cubes:%s, dataset:%s",
                        metric, len(input_pair[1]), dataset)

            model_datasets = {attr['variable_group']:
                              iris.load_cube(attr['filename'])
                              for attr in input_pair[1][dataset]}
            model = sst_regressed(model_datasets[var_group[0]])
            val = np.sqrt(np.mean((obs - model) ** 2))
            metric_values.append((dataset, val))
            model_plot.append(model)

        months = np.arange(1, 73) - 36
        # plot function, xticks, labels as dict/ls
        fig = plot_level1((months, model_plot), (months, obs), metric_values,
                          ['Degree C / C', f'ENSO {metric}', dt_ls])

    return metric_values, fig


def get_prov_rec(caption, plot_type, ancestor_files):
    """Create a provenance record describing the diagnostic data and plot."""
    record = {
        'caption': caption,
        'statistics': ['anomaly'],
        'domains': ['eq'],
        'plot_types': [plot_type],
        'authors': [
            'chun_felicity',
            # 'beucher_romain',
            # 'sullivan_arnold',
        ],
        'references': [
            'access-nri',
        ],
        'ancestors': ancestor_files,
    }
    return record


def main(cfg):
    """Run ENSO metrics."""
    input_data = cfg['input_data'].values()

    # iterate through each metric and get variable group preprocessed data
    metrics = {'lifecycle': ['tos_lifdur1']}

    # select twice with project to get obs, iterate through model selection
    for metric, var_preproc in metrics.items():
        logger.info("Metric: %s, group: %s", metric, var_preproc)
        obs, models = [], []
        for var_prep in var_preproc:
            obs += select_metadata(input_data, variable_group=var_prep,
                                   project='OBS')
            obs += select_metadata(input_data, variable_group=var_prep,
                                   project='OBS6')
            models += select_metadata(input_data, variable_group=var_prep,
                                      project='CMIP6')

        msg = f"{metric}: observation datasets {len(obs)},"
        msg += f"models {pformat(models)}"
        logger.info(msg)

        # obs datasets for each model
        obs_datasets = {datas['variable_group']:
                        iris.load_cube(datas['filename']) for datas in obs}

        # group models by dataset
        model_ds = group_metadata(models, 'dataset', sort='project')

        in_pair = [obs_datasets, model_ds]

        dt_files = [datas['filename'] for datas in obs]
        for dset in models:
            dt_files.append(dset['filename'])
        prov_record = get_prov_rec(f'ENSO metrics {metric}',
                                    'line', dt_files)

        # process function for each metric
        values, fig = compute_enso_metrics(in_pair, obs[0]['dataset'],
                                            var_preproc, metric)
        save_figure(metric, prov_record, cfg,
                    figure=fig, dpi=300)

        # save metric for each pair, check not none
        metricfile = get_diagnostic_filename('matrix', cfg,
                                                extension='csv')
        with open(metricfile, 'a+', encoding='utf-8') as csvfile:
            for dataset, value in values:
                csvfile.write(f"{dataset},{metric},{value}\n")


if __name__ == '__main__':

    with run_diagnostic() as config:
        main(config)
