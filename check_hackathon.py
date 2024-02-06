#!/usr/bin/python3
import os
import grp

required = {

        "oi10": "CMIP6 replicas",
        "fs38": "CMIP6 ACCESS publications",
        "al33": "CMIP5 replicas",
        "rr3": "CMIP5 ACCESS publications",
        "r87": "CMIP3",
        "ct11": "ACCESS-NRI replica collection",
        "xp65": "ACCESS-NRI analysis environments",
        "nf33": "ACCESS-NRI training"
        }



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
    check_read_access("/g/data/xp65/public/apps/esmvaltool")
    check_esmvaltool_config_file_exists()
