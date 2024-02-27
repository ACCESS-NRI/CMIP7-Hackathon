# ACCESS-NRI CMIP7-Hackathon

Welcome to the ACCESS-NRI CMIP7 Hackathon repo.

## Getting Started

To get the most out of the hackathon exercises, we recommend using Microsoft Visual Studio Code which can be downloaded free for Windows, MacOS and Linux [here](https://code.visualstudio.com/). Additionally, for new users or those simply wanting a quick refresher, you can watch our getting started video tutorial here.

The first thing to do is to clone this repo to a location on Gadi that you have permission to use via the following 3 steps: 

Step 1. Log into Gadi using ssh via the command line using your registed NCI *username* and enter your password when prompted. Once you see the welcome note you have successfully logged in. 
```
$ ssh [username]@gadi.nci.org.au
``` 
Step 2. Navigate to the location you wish to use for this hackathon using the *cd* command follwed by the location path.
```
cd [location path]
```
Step 3. Clone the ACCESS-NRI CMIP7 Hackathon repo to this location be entering the following on the command line:
```
git clone https://github.com/ACCESS-NRI/CMIP7-Hackathon
```
When successfully cloned, you will see the directory *CMIP7-Hackathon*. To open this directory, enter the following:
```
cd CMIP7-Hackathon
```
Once inside the CMIP7-Hackathon directory, to make sure your Gadi environment and NCI project permissions are all set up correctly, before starting any of the tutorials, please first run the following *Python* script:

```
python3 check_hackathon.py
```
Please make sure you see a result of "OK" next to each line before proceeding.


## Running an ESMValTool recipe on Gadi

Individual *ESMValTool* recipes can be automatically set up and run on Gadi using the following 1-line command. Simply replace [recipe path] with the relative path to a recipe found in the [recipes folder](https://github.com/ACCESS-NRI/CMIP7-Hackathon/tree/main/recipes).

```
source admin/bash_utilities.sh; run_recipe [recipe path]
```

An example might be:

```
source admin/bash_utilities.sh; run_recipe recipes/ocean/maps/map1.yml
```

If working correctly, you should see:
```
Running recipe: recipes/ocean/maps/map1.yml
107769xxx.gadi-pbs
```
This tells us that, in this case, the *ESMValTool* recipe *map1* has been successfully submitted to Gadi for processing and the job number is 107769xxx. 
To check the status of this job, you can enter either of the following:
```
qstat 107769xxx
```
-- to track the status of a specific job number, or
```
qstat -u [username]
```
-- to track the status of all jobs submitted to the queue by you. Simply replace [username] with your NCI username.
