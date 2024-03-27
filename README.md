# ACCESS-NRI CMIP7-Hackathon

Welcome to the ACCESS-NRI CMIP7 Hackathon repo! Thanks to everyone who joined for our evaluation hackathon, held March 12-14, 2024.

## Links from the hackathon
- [Hackathon agenda](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/Hackathon%20Agenda.pdf)
- [Notes taken during general sessions](https://docs.google.com/document/d/11hlSrGoAdl1qKTZIgGL0BpJhRWoB5nUVB2kf0wxQ06w/edit?usp=share_link) (thanks to Sramana, Dhruv, and Aditya for these excellent notes! :clap:)
- [Summary of all the breakout group notes](https://docs.google.com/document/d/1TzUQmt2eJj1gOr2wSl3WK_LDqBBSFx7-tl4HZeljW7Q/edit?usp=share_link) (collated into a single document)

## Visual Studio Code (VS Code)

To get the most out of the hackathon exercises, we recommend using Microsoft Visual Studio Code which can be downloaded free for Windows, MacOS and Linux [here](https://code.visualstudio.com/). For new VS Code users or those simply wanting a quick refresher, we have created a video and written guide to help you set up VS Code on Gadi. Note that the information is roughly the same, so you can choose either video or written guide to follow along.
- [Video tutorial: Visual Studio Code Workflow for Gadi](https://youtu.be/fSxirzDR3iw) _(~6 min)_
- [Written guide: Getting Started Guide for Visual Studio Code with Gadi](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/1_VSCode_setup_guide_RECOMMENDED.md)


_**NOTE:** There are two pieces of information to clarify from the video tutorial that are explained in the written guide:_
1. _When logging into Gadi for the first time in VS Code, you do not need to write your own config file. You can simply choose the default option that is suggested and VS Code will create one for you. You only need to do this once - the first time you log in._
2. _In addition to the 3 extensions mentioned in the video, you will need to install a 4th extension to view html files (this is how most of the ESMValTool recipes show output plots). You can see our recommended extension "Live Server" in the [written guide above](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md).

## Australian Research Environment (ARE)
If it is not possible to use VS Code, hackathon exercises can alternatively be run via either an [Australian Research Environment](https://are-auth.nci.org.au/) JupyterLab or an [Australian Research Environment](https://are-auth.nci.org.au/) Virtual Desktop (VDI) session. We have created a written guide to setup each of these for the CMIP7-Hackathon below.
- [Written guide: ACCESS-NRI CMIP7-Hackathon ARE JupyterLab setup guide](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/2_ARE_JupyterLab_setup_guide.md).
- [Written guide: ACCESS-NRI CMIP7-Hackathon ARE Virtual Desktop (VDI) setup guide](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/3_ARE_VDI_setup_guide.md).

## Logging into Gadi

The first thing to do is to login to Gadi. You can choose to run the following commands either from your computer's terminal or from the terminal within VS Code. If you follow the above steps to set up VS Code on Gadi, you can skip to the next section ["Set up our environment to run ESMValTool"](#set-up-our-environment-to-run-ESMValTool) below (since the [video](https://youtu.be/fSxirzDR3iw) and [written guide](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md) already walk you through how to connect to Gadi in VS Code). 

Log into Gadi using ssh via the command line using your registed NCI *username* and enter your password when prompted. Once you see the welcome note you have successfully logged in. 
```
$ ssh [username]@gadi.nci.org.au
```
## Set up our environment to run ESMValTool 

Next we want to set up our system to run the ESMValTool recipes prepared for the Hackathon. 

**Step 1.** Enter the following two commands (one after the other). The first command loads some necessary dependencies needed to run ESMValTool, and the second command loads the required [ACCESS-NRI ESMValTool-workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow) module.
```
module use /g/data/xp65/public/modules
```
```
module load esmvaltool
```
**Step 2.** Run the hackathon setup script from any directory. This verifies that your NCI account has access to the required projects on Gadi and that their respective storage locations are mounted, clones the [CMIP7-Hackathon Github repository](https://github.com/ACCESS-NRI/CMIP7-Hackathon), and automatically runs each of the hackathon ESMValTool recipes as PBS jobs on Gadi.
```
check_hackathon
```
You will see a range of checks and processes print to the screen, which may take up to 1 minute to complete. Once you see the "YOU ARE ALL SET!!!" message, everything is setup and ready to go.

## ESMValTool recipes

You have just started running a suite of ESMValTool recipes! You can now do any of the following:

* Check the status of each of your actively running recipes:
```
qstat -u [username]
```
* View ESMValTool recipe outputs here:
```
/scratch/nf33/[username]/esmvaltool_outputs
```
* View ESMValTool recipe log files here:
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

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/tree/main#access-nri-cmip7-hackathon)
