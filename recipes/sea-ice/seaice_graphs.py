"""diagnostic script to plot some graphs based on code
    from Anton's COSIMA cookbook notebook

"""

import cartopy.crs as crs
import xarray as xr
import matplotlib.pyplot as plt
import xesmf
import calendar
import matplotlib.lines as mlines
import numpy as np
import pandas as pd

import os
import logging
from esmvaltool.diag_scripts.shared import run_diagnostic, Datasets, Variables
from esmvaltool.diag_scripts.shared._base import get_plot_filename


# This part sends debug statements to stdout
logger = logging.getLogger(os.path.basename(__file__))

def sea_ice_area(sic,area,coordls, range=[0.15,1]): 
    #percent is in 0-100. Mulitply by portion so divide by 100 ##
    sic = sic/100 
    return (sic*area).where((sic>=range[0])*(sic<=range[1])).sum(coordls)

def sea_ice_area_obs(ds):
    sic=ds.siconc #
    area_km2=ds.areacello/1e6 #
    result=sea_ice_area(sic,area_km2,['x','y']).to_dataset(name='cdr_area') 

    #Theres a couple of data gaps which should be nan
    result.loc[{'time':'1988-01-01'}]=np.nan
    result.loc[{'time':'1987-12'}]=np.nan

    return result.sel(time=slice('1979','2018')) 

def sea_ice_area_model_sh(ds):
    sic = ds.siconc.where(ds.siconc.lat < -20, drop=True) #
    
    area_km2=ds.areacello/1e6 ##area convert to km2

    return sea_ice_area(sic,area_km2,['i','j']).to_dataset(name='si_area')

def min_and_max(ds):
    def min_and_max_year(da):
        result = xr.Dataset()
        result['min']=da.min()
        result['max']=da.max()
        return result
    annual_min_max_ds=ds.si_area.groupby('time.year').apply(min_and_max_year)
    return annual_min_max_ds

def plot_trend(model_min_max_dt, obs_a, minmax):
    """
    cube: iris cube of precipitaion anomalies with only time dimension.
    change to xarray
    """

    figure, axes = plt.subplots()
    
    # both min and max # multiple models? 
    # add note for years change?
    model_min_max_dt[minmax].plot(label='ACCESS-OM2')

    if minmax == 'max':
        obs_a.cdr_area.groupby('time.year').max().plot(label='Obs CDR')
        plt.title('Trends in Sea-Ice Maxima')
    elif minmax == 'min':
        obs_a.cdr_area.groupby('time.year').min().plot(label='Obs CDR')
        plt.title('Trends in Sea-Ice Minima')

    
    plt.ylabel('Sea-Ice Area (km2)')

    _ = plt.legend()
    return figure


def map_diff(mod_si, obs_si):

    ## regridder
    latmax = obs_si.lat.max().values.item()
    lat_min = mod_si.lat.min().values.item()
    mod_si = mod_si.where(mod_si.lat <latmax, drop=True)
    regrd_out = obs_si.where(obs_si.lat > lat_min, drop=True)

    regridder_ACCESSOM2_sh = xesmf.Regridder(
        mod_si.isel(time=0).drop(['i','j']), 
        regrd_out.isel(time=0), 
        'bilinear', 
        periodic=True,
        unmapped_to_nan=True
    )
    months = [2,9]
    # fig set up
    figure = plt.figure(figsize=(6,len(months)*3))
    i=1
    for mon in months:
        cdr = obs_si.siconc.sel(time=obs_si.siconc.time.dt.month.isin(mon)).mean('time')
        da = mod_si.siconc.sel(time=mod_si.siconc.time.dt.month.isin(mon)).mean('time')
        
        mod_regrid = regridder_ACCESSOM2_sh(da)
        diff_ds = mod_regrid - cdr

        ax = plt.subplot(2, 2, i, projection=crs.SouthPolarStereo(true_scale_latitude=-70)) #
   
        diffmap = ax.contourf( 
            diff_ds.x, diff_ds.y, diff_ds, 
            levels=np.arange(-90,91,20), cmap='RdBu' #cmo.balance_r (import cmocean.cm as cmo)
        )
        cs_cdr = cdr.plot.contour(levels=[15], ax=ax)
        cs_mod = mod_regrid.plot.contour(levels=[15], ax=ax, colors=['black'])
        
        plt.title(calendar.month_name[mon])
        i+=2

    color_cdr = cs_cdr.collections[0].get_edgecolor()
    line_cdr = mlines.Line2D([], [], color=color_cdr, label="Observed Extent")

    color_mod = cs_mod.collections[0].get_edgecolor()
    line_mod = mlines.Line2D([], [], color=color_mod, label="Modelled Extent")

    plt.legend(handles=[line_cdr,line_mod], loc='center left', bbox_to_anchor=(1.2,0.5))
    cax = plt.axes([0.6,0.55,0.05,0.3])
    _ = plt.colorbar(diffmap, cax=cax, label='Difference in \nSea Ice Concentration')
    return figure

def main(cfg):
    """Compute sea ice area for each input dataset."""

    input_data = cfg['input_data'].values()
    variables = Variables(cfg)

    data = []
    logger.info(f"!!! {df} variables: {variables}.. !!")

    # Ex
    for dataset in input_data:
        # Load the data
        input_file = [dataset['filename'], dataset['short_name'], dataset['dataset']]
        # key for different models      
        logger.info(f"dataset: {dataset['long_name']}")
        data.append(input_file)

    df = pd.DataFrame(data, columns=['filename','short_name','dataset']) #

    logger.info(df)
    for fp,sn, dt in df.itertuples(index=False):
        if dt == 'ACCESS-OM2':  # other models?
            if sn == 'areacello':
                area_mod = xr.open_dataset(fp) 
            else:
                mod_si = xr.open_dataset(fp)
        elif dt == 'NSIDC-G02202-sh':    
            if sn == 'areacello':
                area_obs = xr.open_dataset(fp) 
            else:
                obs_si = xr.open_dataset(fp)
    
    obs_si['areacello'] = area_obs['areacello']
    obs_a = sea_ice_area_obs(obs_si)

    mod_si['areacello'] = area_mod['areacello']
    model_area_dt = sea_ice_area_model_sh(mod_si)    
    model_min_max_dt = min_and_max(model_area_dt)
    model_min_max_dt['year'] = model_min_max_dt.year + 1652  # make years compariable

    for m in ['min','max']:  
        fig = plot_trend(model_min_max_dt, obs_a, m)
        # Save output
        output_path = get_plot_filename(f'{m}_trend', cfg)
        fig.savefig(output_path) 

    logger.info("creating map differences")
    mapfig = map_diff(mod_si,obs_si)
    # Save output
    output_path = get_plot_filename('map_difference', cfg)
    mapfig.savefig(output_path) 

if __name__ == '__main__':

    with run_diagnostic() as config:
        main(config)
