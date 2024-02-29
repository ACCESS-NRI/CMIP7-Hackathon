# Getting started guide for Visual Studio Code
<p>This is an introductory guide to setting up and using Microsoft Visual Studio Code to interact with Gadi and run ESMValTool recipes for the ACCESS-NRI CMIP7-Hackathon.</p>

## Quick-links to sections
- [0. Pre-Workshop preparation](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#0-pre-workshop-preparation)
- [1. Installing VS Code extensions](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#1-installing-vs-code-extensions)
- [2. Open remote connection to Gadi](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#2-open-remote-connection-to-gadi)
- [3. Load ESMValTool modules and set up Hackathon environment](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#3-load-esmvaltool-modules-and-set-up-hackathon-environment)
- [4. Create a workspace / open folders on Gadi](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#4-create-a-workspace--open-folders-on-gadi)
- [5. VS Code extras](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#5-vs-code-extras)

## 0. Pre-workshop preparation

- *0.1* In order to get the most out of the Hackathon, you will require a NCI account. If you do not yet have a NCI account, you can sign up on the [MyNCI website](https://my.nci.org.au).
- *0.2* To run the exercises, access to specific projects on Gadi is required. To help things run as smoothly as possible on the day, please log in to the [MyNCI website](https://my.nci.org.au) and join the following projects:
`nf33`, `xp65`, `fs38`, `oi10`, `al33`, `rr3`, `rt52`, `zz93` and `ct11` **prior** to attending the Hackathon. Please note it can take 1-2 days to receive membership approvals.
- *0.3* Download and install Microsoft Visual Studio on your local system. VS Code can be downloaded from [this page](https://code.visualstudio.com/).

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#getting-started-guide-for-visual-studio-code)

## 1. Installing VS Code extensions
Out of the box, VS Code doesn't do everything we need it to - so we must install some software extensions to get the most out of the Hackathon.

- *1.1* When VS Code starts up, you are greeting with a GUI that looks like this. The first thing we need to do is click the extensions icon in the left-hand navigation pane marked below with the red ellipse.

<p align="center"><img src="assets/extensions.png" alt="drawing" width="90%"/></p>

We have a total of 4 extensions to install. Note that when hovering over a listed extension, a small information pane pops up, and clicking on an extension opens a full extension information page.

- *Extension 1:* **Python** <br>
This extension provides full code support and highlighting for the *Python* programming language within VS Code. Type `python` into the extensions search bar and select the *Python* extension published by Microsoft marked with the red ellipse below. Click `install` to add the extension.

<p align="center"><img src="assets/extensions_python.png" alt="drawing" width="90%"/></p>

- *Extension 2:* **Jupyter** <br>
This extension allows us to view, edit and run *Jupyter Notebooks* within VS Code. Type `jupyter` into the extensions search bar and select the *Jupyter* extension published by Microsoft marked with the red ellipse below. Click `install` to add the extension.

<p align="center"><img src="assets/extensions_jupyter.png" alt="drawing" width="90%"/></p>

- *Extension 3:* **Remote-SSH** <br>
This extension allows us to securely login in remote servers, in our case NCI Gadi, using *ssh*. Type `remote ssh` into the extensions search bar and select the *Remote-SSH* extension published by Microsoft marked with the red ellipse below. Click `install` to add the extension.

<p align="center"><img src="assets/extensions_ssh.png" alt="drawing" width="90%"/></p>

- *Extension 4:* **Live Server** <br>
Type `live server` into the extensions search bar and select the *Live Server* extension published by Ritwick Dey marked with the red ellipse below. Click `install` to add the extension.

<p align="center"><img src="assets/extensions_liveserver.png" alt="drawing" width="90%"/></p>

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#getting-started-guide-for-visual-studio-code)

## 2. Open remote connection to Gadi

To connect to Gadi, follow these steps to establish and open a remote connection using the *Remote-SSH* extension.

- *2.1* To get started, click the blue `Open a Remote Window` button in the bottom left-hand corner.

<p align="center"><img src="assets/open_remote1.png" alt="drawing" width="90%"/></p>

- *2.2* Select `Connect Current Window to Host...` to open the connection to Gadi within the current window. Alternatively, you can select `Connect to Host...` to open the connection in a new window.

<p align="center"><img src="assets/open_remote2.png" alt="drawing" width="90%"/></p>

- *2.3* Click `+ Add New SSH Host`

<p align="center"><img src="assets/open_remote3.png" alt="drawing" width="90%"/></p>

- *2.4* Enter the remote host (Gadi) details which are comprised of your NCI `username` followed by `@gadi.nci.org.au`. You may be prompted to select a _ssh_ `config` file so VS Code can remember your _ssh_ connections in future. Usually the first option works fine as VS Code will manage the file.

<p align="center"><img src="assets/open_remote4.png" alt="drawing" width="90%"/></p>

- *2.5* You will then be prompted to enter your NCI account password. Once connected, the blue button in the bottom left-hand corner will say `SSH: gadi.nci.org.au`. VS Code also automatically opens a live terminal (bottom right) in your `/home` folder. Great news, you are now connected to Gadi!

<p align="center"><img src="assets/open_remote5.png" alt="drawing" width="90%"/></p>

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#getting-started-guide-for-visual-studio-code)

## 3. Load ESMValTool modules and set up Hackathon environment

To load all required ESMValTool and [ACCESS-NRI ESMValTool-workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow) components, please enter the following two commands (one after the other) in the terminal from any directory:

```
module use /g/data/xp65/public/modules [then press ENTER/RETURN]
```
followed by:
```
module load esmvaltool [then press ENTER/RETURN]
```

To set up the Hackathon environment (check project membership, mount required storage, created working folders and clone the Hackathon Github repository), please enter the following command in the terminal from any directory:
```
check_hackathon [then press ENTER/RETURN]
```
You will see a range of checks and processes print to the screen. Once you see the "YOU ARE ALL SET!!!" message, everything is setup and ready to go.
<br><br>
This process also creates and runs a PBS job on Gadi for each of the Hackathon example ESMValTool recipes. To check the status of these jobs enter the following into the terminal - where [username] is your NCI account username.
```
qstat -u [username]
```
This will list all currently running ESMValTool recipes.
<br><br>
For each, recipe outputs can be found in:
```
/scratch/nf33/[username]/esmvaltool_outputs
```
and associated log files can be found in:
```
/scratch/nf33/[username]/MIP7-Hackathon/admin/logs
```
The full cloned [CMIP7-Hackathon Github repository](https://github.com/ACCESS-NRI/CMIP7-Hackathon) can be found here:
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
[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#getting-started-guide-for-visual-studio-code)

## 4. Create a workspace / open folders on Gadi

VS Code allows you to create custom workspaces, which is particularly convenient for quick access to multiple directories/folders on Gadi which may be located in different locations.

- *4.1* To add a directory/folder to the current workspace, simply click the `Open Folder` button marked in red below. Alternatively, you can also add folders via `File > Open Folder`.

<p align="center"><img src="assets/workspace1.png" alt="drawing" width="90%"/></p>

- *4.2* You will then be prompted to add a valid path on Gadi to the folder you wish to add. In this example, we are adding the path to your main Hackathon folder `/scratch/nf33/[username]/CMIP7-Hackathon` created by running `check_hackathon` above. Once you have entered the path, press `OK`. N.B. When adding a folder, VS Code may request you re-enter your NCI account password.

<p align="center"><img src="assets/workspace2.png" alt="drawing" width="90%"/></p>

Once this is done, the folder will be visible in the left-hand `EXPLORER` pane (and can be expanded to show all contents), it is also displayed at the top of page in the search bar (allowing quick searches of the selected folder), and the terminal also opens in the selected folder (the `ls` command is shown here to list the folder contents).

<p align="center"><img src="assets/workspace3.png" alt="drawing" width="90%"/></p>

You can add multiple unique folders to the current workspace by right clicking and selecting `Add folder to Workspace` and following the process described above in section 4.2.

<p align="center"><img src="assets/workspace4.png" alt="drawing" width="90%"/></p>

Now that you have a workspace setup, why not add the above mentioned `esmvaltool_outputs` and `logs` folders (replacing [username] with your NCI account username) for quick access.

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#getting-started-guide-for-visual-studio-code)

## 5. VS Code extras

To open any supported file(s), you can double click it in the left-hand `EXPLORER` pane or drag-and-drop it into the main panel. To add a second main panel, right-click any extra files in `EXPLORER` and select `Open to the Side`.

<p align="center"><img src="assets/files.png" alt="drawing" width="90%"/></p>

Along with folders in a workspace, you can also have multiple independent terminal sessions running at the same time. To do this, click the `+` button at the top right of a terminal panel.
<br>
<br>
If you have multiple folders open in your workspace, you will first be prompted to `Select current working directory for new terminal` at the top.

<p align="center"><img src="assets/terminals.png" alt="drawing" width="90%"/></p>

[\[Back to top\]](https://github.com/ACCESS-NRI/CMIP7-Hackathon/blob/main/docs/VSCode_setup_guide.md#getting-started-guide-for-visual-studio-code)
