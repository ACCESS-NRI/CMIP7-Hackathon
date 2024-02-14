"""
ESMValTool port of ENSO analysis plotting script by Arnold Sullivan (CSIRO)
"""

import xarray as xr
import numpy as np
from matplotlib import pyplot as plt
import os
import pandas as pd

# EOF 
#import sacpy as scp
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
#import sacpy.Map as smap
from scipy.linalg import svd

# ESMValTool requirements
import logging
from esmvaltool.diag_scripts.shared import run_diagnostic, Datasets, Variables
from esmvaltool.diag_scripts.shared._base import get_plot_filename

# This part sends debug statements to stdout
logger = logging.getLogger(os.path.basename(__file__))


## ------------------------------


# Main functions
def plot_eof2(ssta,ttl,fName,xlon,xlat):
    '''
    # Example usage:
    # Assuming you have a variable 'ssta'
    ssta = n3_anom1.ts
    plot_eof(ssta)
    pcs_amo = plot_eof2(AMO,ttl,fName,310,40)
    '''
    eof = scp.EOF(np.array(ssta))
    eof.solve()
    pc = eof.get_pc(npt=2)
    pt = eof.get_pt(npt=2)

    lon, lat = np.array(ssta.lon), np.array(ssta.lat)

    # Check and ensure positive pt at 90W 0N
    lon_index = np.abs(lon - xlon).argmin()  # Find the index for 120W
    lat_index = np.abs(lat - xlat).argmin()    # Find the index for 0N

    if pt[0, lat_index, lon_index] < 0:
        pt[0] *= -1
        pc[0] *= -1
    if pt[1, lat_index, lon_index] < 0:
        pt[1] *= -1
        pc[1] *= -1

    fig = plt.figure(figsize=[12, 7])
    ax = fig.add_subplot(221)
    m1 = ax.contourf(lon, lat, pt[0, :, :], cmap=shayne_cmap, levels=np.linspace(-0.75, 0.75, 15), extend="both")
    ax.contour(m1, colors="black")
    ax.set_title(ttl[0])
    ax2 = fig.add_subplot(222)
#    ax2.plot(ssta.time, pc[0])
    ax2.plot(pc[0])
    ax2.grid()
    ax2.set_title(ttl[1])
    ax3 = fig.add_subplot(223) #, projection=ccrs.PlateCarree(central_longitude=180))
    m2 = ax3.contourf(lon, lat, pt[1, :, :], cmap=shayne_cmap, levels=np.linspace(-0.75, 0.75, 15), extend="both")
    ax3.contour(m2, colors="black")
    ax3.set_title(ttl[2])
    ax4 = fig.add_subplot(224)
#    ax4.plot(ssta.time, pc[1])
    ax4.plot(pc[1])
    ax4.grid()
    ax4.set_title(ttl[3])

    cb_ax = fig.add_axes([0.1, 0.06, 0.4, 0.02])
    fig.colorbar(m1, cax=cb_ax, orientation="horizontal")

    plt.savefig(fName+".png",dpi=300)
    plt.show()

    # Return the PCs as a tuple
    return pc

def detrend_dim(da, dim, deg=1):
    # detrend along a single dimension
    p = da.polyfit(dim=dim, deg=deg)
    fit = xr.polyval(da[dim], p.polyfit_coefficients)
    return da - fit

def calculate_n3_anom(var, ystart, ylast):
    ystart_str = str(ystart).zfill(4)
    ylast_str = str(ylast).zfill(4)
    var = var.sel(time=slice(ystart_str, ylast_str))
    var_clim = var.groupby("time.month").mean(dim="time")
    var_anom = var.groupby("time.month") - var_clim
    return var_anom, var_clim


def quick_contour(fig, ax, T1, mag_max):
    '''
    fig, axs = plt.subplots(2, 2, figsize=(16, 8), subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)})

    # Assuming T1 is a 2D array, you need to choose the appropriate subplot
    ax1 = axs[0, 0]  # Adjust this based on your requirements
    ax1, cbar1 = quick_contour(fig, ax, T1, mag_max)

    '''
    x = T1.lon - 180
    y = T1.lat
    
    # Plot T1 as a pcolormesh plot
    pcm = ax.pcolormesh(x, y, T1, vmax=mag_max, vmin=-1 * mag_max, cmap=shayne_cmap)
    
    # Add coastlines
    ax.coastlines(color='gray', linewidth=3)
    
    # Set latitude and longitude ticks
    ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
    ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
    
    # Set tick label font size
    ax.tick_params(axis='both', labelsize=12)
    
    # Add colorbar
    cbar = fig.colorbar(pcm, ax=ax, orientation='vertical', pad=0.1)
    cbar.set_label('T1 Colorbar Label')  # Change the label as needed
    return ax, cbar


from matplotlib.colors import LinearSegmentedColormap
# Define the colors for the colormap
colors = [
    (0.0000000e+00, 0.0000000e+00, 1.0000000e+00),
    (1.0000000e-01, 1.0000000e-01, 1.0000000e+00),
    (2.0000000e-01, 2.0000000e-01, 1.0000000e+00),
    (3.0000000e-01, 3.0000000e-01, 1.0000000e+00),
    (4.0000000e-01, 4.0000000e-01, 1.0000000e+00),
    (5.0000000e-01, 5.0000000e-01, 1.0000000e+00),
    (6.0000000e-01, 6.0000000e-01, 1.0000000e+00),
    (7.0000000e-01, 7.0000000e-01, 1.0000000e+00),
    (8.0000000e-01, 8.0000000e-01, 1.0000000e+00),
    (9.0000000e-01, 9.0000000e-01, 1.0000000e+00),
    (1.0000000e+00, 1.0000000e+00, 1.0000000e+00),
    (1.0000000e+00, 9.0000000e-01, 9.0000000e-01),
    (1.0000000e+00, 8.0000000e-01, 8.0000000e-01),
    (1.0000000e+00, 7.0000000e-01, 7.0000000e-01),
    (1.0000000e+00, 6.0000000e-01, 6.0000000e-01),
    (1.0000000e+00, 5.0000000e-01, 5.0000000e-01),
    (1.0000000e+00, 4.0000000e-01, 4.0000000e-01),
    (1.0000000e+00, 3.0000000e-01, 3.0000000e-01),
    (1.0000000e+00, 2.0000000e-01, 2.0000000e-01),
    (1.0000000e+00, 1.0000000e-01, 1.0000000e-01),
    (1.0000000e+00, 0.0000000e+00, 0.0000000e+00)
]

# Create the colormap
shayne_cmap = LinearSegmentedColormap.from_list("shayne_cmap", colors)


## ------------------------------






## ------------------------------


def main(cfg):

    """Generate plots"""
    input_data = cfg['input_data'].values()
    data = []

    # Find input datasets to use
    for dataset in input_data:
        
        input_file = [dataset['filename'], dataset['dataset']]
        # drop areacello dataset for map
        # if dataset['short_name'] == 'siconc':
        data.append(input_file)

    df = pd.DataFrame(data, columns=['filename','dataset'])

    logger.info(df)



if __name__ == '__main__':

    with run_diagnostic() as config:
        main(config)