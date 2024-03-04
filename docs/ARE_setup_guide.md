# ACCESS-NRI CMIP7-Hackathon ARE setup guide
<p>Quick-start guide to setting up a JupyterLab session using the Australian Research Environment to run the ACCESS-NRI CMIP7-Hackathon exercises.</p>

## Quick-links to sections
- [0. Pre-Workshop preparation](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#0-pre-workshop-preparation)
- [1. Open ARE on Gadi](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#1-installing-vs-code-extensions)
- [2. Start JupyterLab App](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#2-open-remote-connection-to-gadi)
- [3. Configure JupyterLab session](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#3-load-esmvaltool-modules-and-set-up-hackathon-environment)
- [4. Launch JupyterLab session](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#4-create-a-workspace--open-folders-on-gadi)
- [5. Setup Hackathon ESMValTool environment](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#5-vs-code-extras)

## 0. Pre-workshop preparation

- *0.1* In order to get the most out of the Hackathon, you will require a NCI account. If you do not yet have a NCI account, you can sign up on the [MyNCI website](https://my.nci.org.au).
- *0.2* To run the exercises, access to specific projects on Gadi is required. To help things run as smoothly as possible on the day, please log in to the [MyNCI website](https://my.nci.org.au) and join the following projects:
`nf33`, `xp65`, `fs38`, `oi10`, `al33`, `rr3`, `rt52`, `zz93` and `ct11` **prior** to attending the Hackathon. Please note it can take 1-2 days to receive membership approvals.

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/ARE_setup_guide.md#access-nri-cmip7-hackathon-are-setup-guide)

## 1. Open ARE on Gadi
Go to the [Australian Research Environment](https://are-auth.nci.org.au/) website and login with your **NCI username and password**. If you don't have an NCI account, you can sign up for one at the [MyNCI website](https://my.nci.org.au).

<p align="center"><img src="assets_ARE/login.png" alt="drawing" width="60%"/></p>

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/ARE_setup_guide.md#access-nri-cmip7-hackathon-are-setup-guide)

## 2. Start JupyterLab App
Click on `JupyterLab` under *Featured Apps* to configure a new JupyterLab instance. This option is also available under the *All Apps* section at the bottom of the page and the *Interactive Apps* dropdown located in the top menu.

<p align="center"><img src="assets_ARE/jupyter_select.png" alt="drawing" width="60%"/></p>

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/ARE_setup_guide.md#access-nri-cmip7-hackathon-are-setup-guide)

## 3. Configure JupyterLab session
You will now be presented with the main JupyterLab instance configuration form. Please complete **only** the fields below - leave all other fields blank or to their default values.

- *3.1* **Walltime**: The number of hours the JupyterLab instance will run. For the hackathon, please insert a walltime of `4` hours.

<p align="center"><img src="assets_ARE/walltime.png" alt="drawing" width="60%"/></p>

- *3.2* **Compute Size**: Select `Medium (4 cpus, 18G mem)` from the dropdown menu.

<p align="center"><img src="assets_ARE/compute.png" alt="drawing" width="60%"/></p>

- *3.3* **Project**: Please enter `nf33`. This will allocate SU usage to the workshop project.

<p align="center"><img src="assets_ARE/project.png" alt="drawing" width="60%"/></p>

- *3.4* **Storage**: This is the list of project data storage locations required to complete the hackathon exercises. In ARE, storage locations need to be explicitly defined to access these data from within a JupyterLab instance. Please copy and paste the following string listing into the storage input field:
```
scratch/nf33+gdata/nf33+gdata/xp65+gdata/fs38+gdata/oi10+gdata/al33+gdata/rr3+gdata/rt52+gdata/zz93+gdata/ct11
```

<p align="center"><img src="assets_ARE/project.png" alt="drawing" width="60%"/></p>

- *3.5* Click `Advanced options ...`
  * Optional: You can check the box here to receive an email notification when your JupyterLab instance starts, but as we are running a relatively small instance, it will likely spin up quickly so this probably isn't necessary.</p>

- *3.6* **Module directories**: To load the required environment modules, please copy and paste the following. This is equivalent to using `module use` on the command line.
```
/g/data/xp65/public/modules
```

<p align="center"><img src="assets_ARE/module_directories.png" alt="drawing" width="60%"/></p>

- *3.7* **Modules** To load the ESMValTool-workflow environment, please copy and paste the following. This is equivalent to using `module load` on the command line.
```
esmvaltool
```

<p align="center"><img src="assets_ARE/modules.png" alt="drawing" width="60%"/></p>

- *3.7* Click `Launch` to start your JupyterLab instance.


<p align="center"><img src="assets_ARE/launch.png" alt="drawing" width="60%"/></p>

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/ARE_setup_guide.md#access-nri-cmip7-hackathon-are-setup-guide)

## 4. Launch JupyterLab session
Once you have clicked `Launch` the browser will redirect to the 'interactive sessions' page where you will see your JupyterLab instance details and current status which will look something like this:

<p align="center"><img src="assets_ARE/queue.png" alt="drawing" width="60%"/></p>

Once the JupyterLab instance has started (this usually takes around 30 seconds) and this status window should update and look something like the following, reporting that the instance has started and the time remaining. More detailed information on the instance can be accessed by clicking the `Session ID` link.

<p align="center"><img src="assets_ARE/running.png" alt="drawing" width="60%"/></p>

Click `Open JupyterLab`. This opens the instance a new browser window where you can navigate to the location of the cloned tutorial files.

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/ARE_setup_guide.md#access-nri-cmip7-hackathon-are-setup-guide)

## 5. Setup Hackathon ESMValTool environment
To finalise the system setup, we must run the hackathon setup script. This verifies that your NCI account has access to the required projects on Gadi and that their respective storage locations are mounted, clones the [CMIP7-Hackathon Github repository](https://github.com/ACCESS-NRI/CMIP7-Hackathon), and automatically runs each of the hackathon ESMValTool recipes as PBS jobs on Gadi.

To do this within ARE, from the `Launcher` window we must first open `Terminal`:

<p align="center"><img src="assets_ARE/terminal.png" alt="drawing" width="80%"/></p>

Once the terminal is open, insert the following command and press `ENTER/RETURN`:

```
check_hackathon
```

When successful, you will see a range of checks and processes print to the screen, which may take up to 1 minute to complete. Once you see the "YOU ARE ALL SET!!!" message, everything is setup and ready to go.

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/ARE_setup_guide.md#access-nri-cmip7-hackathon-are-setup-guide)
