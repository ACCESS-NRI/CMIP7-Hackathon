#!/usr/bin/python3
import os
import grp
import subprocess
from pathlib import Path

required = {

        "oi10": "CMIP6 replicas",
        "fs38": "CMIP6 ACCESS publications",
        "al33": "CMIP5 replicas",
        "rr3": "CMIP5 ACCESS publications",
        "ct11": "ACCESS-NRI replica collection",
        "xp65": "ACCESS-NRI analysis environments",
        "nf33": "ACCESS-NRI training"
        }


pbs_job = """#!/bin/bash -l 
#PBS -S /bin/bash
#PBS -P iq82
#PBS -l storage=gdata/fs38+gdata/oi10+gdata/rr3+gdata/xp65+gdata/al33+gdata/rt52+gdata/zz93+scratch/nf33+gdata/ct11
#PBS -l wd
#PBS -q copyq
#PBS -l walltime=04:00:00
#PBS -l mem=64GB
#PBS -l ncpus=1

module use /g/data/xp65/public/modules
module load esmvaltool

esmvaltool run --output_dir=/scratch/nf33/\$USER/esmvaltool_outputs \$recipe
"""

def run_recipe(recipe_path):

    if os.path.isfile(recipe_path):
        recipe_name=Path(recipe_path).stem
        subprocess.run(f"qsub -v recipe={recipe_path} -N{recipe_name} -e admin/logs/{recipe_name}.stderr -o admin/logs/{recipe_name}.stdout <<< \"{pbs_job}\"", shell=True)
        print(f"Running recipe: {recipe_path}")
    else:
        print("{recipe_path} does not exist, please check the path.")


def user_belong_to_group(group):
    user_groups = [grp.getgrgid(g).gr_name for g in os.getgroups()]
    if group in user_groups:
        return True
    else:
        return False


def check_all_required_group_memberships(groups):
        
    for group, description in required.items():
        if user_belong_to_group(group):
            print(f"{group} OK")
        else:
            print(f"{group} not OK")

def check_read_access(path):
    print(f"Checking that you have read access on all the files in {path}")
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if not os.access(os.path.join(root, name), os.R_OK):
                print("Missing read access")
        for name in dirs:
            if not os.access(os.path.join(root, name), os.R_OK):
                print("Missing read access")


def test_gdata_projects_are_mounted(groups):

    for group, _ in required.items():
        if user_belong_to_group(group):
            if os.path.exists(f"/g/data/{group}"):
                print(f"gdata {group} is mounted")
            else:
                print(f"gdata {group} is not mounted")

def test_training_scratch_project_is_mounted(proj):

    if user_belong_to_group(proj):
        if os.path.exists(f"/scratch/{proj}"):
            print(f"scratch {proj} is mounted")
        else:
            print(f"scratch {proj} is not mounted")

def check_esmvaltool_config_file_exists():
    print(f"Checking that the esmvaltool config file exist")
    if not os.path.exists(os.path.join(os.path.expanduser('~'), ".esmvaltool/config-user.yml")):
        print("ESMValTool config file is missing")


if __name__ == '__main__':
    check_all_required_group_memberships(required)
    test_gdata_projects_are_mounted(required)
    test_training_scratch_project_is_mounted("nf33")
    #check_read_access("/g/data/xp65/public/apps/esmvaltool")
    check_esmvaltool_config_file_exists()
    #run_recipe("./recipes/general/recipe_monitor.yml")
