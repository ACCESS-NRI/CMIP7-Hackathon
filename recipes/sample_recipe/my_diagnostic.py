"""Python example diagnostic.
simplified python diagnostic to fill in with own code

see another example here:
https://github.com/ESMValGroup/ESMValTool/blob/main/esmvaltool/diag_scripts/examples/diagnostic.py
"""

# place your module imports here:

import os
import logging
from pathlib import Path
from pprint import pformat

import matplotlib.pyplot as plt
import iris

# import esmvaltool convenience functions
# run_diagnostic required
from esmvaltool.diag_scripts.shared import (
    group_metadata,
    run_diagnostic,
)


# This part sends debug statements to stdout
logger = logging.getLogger(Path(__file__).stem)


def compute_diagnostic(filename):
    """Compute an example diagnostic."""
    logger.debug("Loading %s", filename)
    cube = iris.load_cube(filename)
    # !! data can be read in other python modules !!

    # !! add in any code to do anything you want to do !!
    logger.debug("Running example computation")

    # example ...
    # cube = iris.util.squeeze(cube)
    return cube


def plot_diagnostic(cube, dataset, cfg):
    # !! alter parameters with what you want, 
    # eg. using xarray dataset
    """Plot diagnostic data."""

    plot_path = cfg['plot_dir']
    # !! set up as you need !!

    # plotting example, cube to fit plotting in arbitrary way
    cube = cube.collapsed(cube.coords()[1:], iris.analysis.MEAN)
    logger.info(cube)
    plt.plot(cube.data, label=dataset)
    plt.xlabel(cube.coords()[0].name())
    plt.ylabel(cube.name())

    png_name = dataset + '.png'
    plt.savefig(os.path.join(plot_path, png_name))
    plt.close()

    return


def main(cfg):
    """Compute the time average for each input dataset."""
    # Get a description of the preprocessed data that we will use as input.
    input_data = cfg['input_data'].values()

    groups = group_metadata(input_data,'variable_group', sort='dataset')
    logger.info(
        "Example of how to group and sort input data by variable groups from "
        "the recipe:\n%s", pformat(groups))

    # Example of how to loop over variables/datasets

    for group_name in groups:
        logger.info("Processing variable %s", group_name)
        for attributes in groups[group_name]:
            logger.info("Processing dataset %s", attributes['dataset'])
            input_file = attributes['filename']
            
            # run compute defined in function above
            cube = compute_diagnostic(input_file)

            # plot computed as defined in function above with label
            out_dataset = group_name + '_' + attributes['dataset']
            plot_diagnostic(cube, out_dataset, cfg)


if __name__ == '__main__':

    with run_diagnostic() as config:
        main(config)
