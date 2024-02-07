# CMIP7-Hackathon

Individual ESMValTool recipes can be automatically set up and run on Gadi using the following 1-line command. Simply replace [recipe path] with the relative path to a recipe found in the [recipes folder](https://github.com/ACCESS-NRI/CMIP7-Hackathon/tree/main/recipes).

```
source admin/bash_utilities.sh; run_recipe [recipe path]
```

An example might be:

```
source admin/bash_utilities.sh; run_recipe recipes/ocean/maps/map1.yml
```
