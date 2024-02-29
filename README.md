# ACCESS-NRI CMIP7-Hackathon

Welcome to the ACCESS-NRI CMIP7 Hackathon repo.

## Visual Studio Code

To get the most out of the hackathon exercises, we recommend using Microsoft Visual Studio Code which can be downloaded free for Windows, MacOS and Linux [here](https://code.visualstudio.com/). Additionally, for new VS Code users or those simply wanting a quick refresher, you can;
- watch our getting started workflow for Gadi video tutorial [here](https://youtu.be/fSxirzDR3iw) (6 min),
- follow our step-by-step getting started guide [here](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md).

## Getting Started

The first thing to do is setup our system to run the ESMValTool recipes prepared for the Hackathon. 

**Step 1.** Log into Gadi using ssh via the command line using your registed NCI *username* and enter your password when prompted. Once you see the welcome note you have successfully logged in. 
```
$ ssh [username]@gadi.nci.org.au
```
**Step 2.** Enter the following two commands (one after the other). The first command loads some necessary dependencies needed to run ESMValTool, and the second command loads the required [ACCESS-NRI ESMValTool-workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow) module.
```
module use /g/data/xp65/public/modules
```
```
module load esmvaltool
```
**Step 3.** Run the hackathon setup script. This verifies that your NCI account has access to the required projects on Gadi and that their respective storage locations are mounted, clones the [CMIP7-Hackathon Github repository](https://github.com/ACCESS-NRI/CMIP7-Hackathon), and automatically runs each of the hackathon ESMValTool recipes as a PBS job on Gadi.
```
check_hackathon
```
Note that this may take up to a minute to finish running.

## ESMValTool recipes

Once you have run `check_hackathon` and have recieved the "YOU ARE ALL SET!!!" message in your chosen terminal, you can now do the following:

* Check the status of each of your actively running recipes:
```
qstat -u [username]
```
* View ESMValTool recipe outputs here:
```
/scratch/nf33/[username]/esmvaltool_outputs
```
* View ESMValTool recipe logs here:
```
/scratch/nf33/[username]/CMIP7-Hackathon/admin/logs
```
* Find the full cloned [CMIP7-Hackathon Github repository](https://github.com/ACCESS-NRI/CMIP7-Hackathon) here:
```
/scratch/nf33/[username]/CMIP7-Hackathon
```
We also include a convenience wrapper function to manually run individual recipes found in the CMIP7-Hackathon Github repository [recipes directory](https://github.com/ACCESS-NRI/CMIP7-Hackathon/tree/main/recipes):
```
run_recipe [path-to-recipe]
```
For example, to manually run the hackathon `map1` recipe found in `/scratch/nf33/[username]/CMIP7-Hackathon/recipes/ocean/maps`, you can `cd` into the cloned CMIP7-Hackathon Github repository
```
cd /scratch/nf33/[username]/CMIP7-Hackathon
```
and run the following:
```
run_recipe recipes/ocean/maps/map1.yml
```
