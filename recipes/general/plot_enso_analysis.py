# ESMValTool port of ENSO analysis plotting script by Arnold Sullivan (CSIRO)

import xarray as xr
import numpy as np
from matplotlib import pyplot as plt

# EOF 
import sacpy as scp
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import sacpy.Map as smap
from scipy.linalg import svd

# ESMValTool requirements
import logging
from esmvaltool.diag_scripts.shared import run_diagnostic, Datasets, Variables
from esmvaltool.diag_scripts.shared._base import get_plot_filename

# This part sends debug statements to stdout
logger = logging.getLogger(os.path.basename(__file__))



## Main plotting functions to be added here after testing



def main(cfg):

    """Generate plots"""
    input_data = cfg['input_data'].values()
    data = []

    selection = select_metadata(input_data)
    logger.info("Testing if data is found and loading:\n%s",
                pformat(selection))


if __name__ == '__main__':

    with run_diagnostic() as config:
        main(config)