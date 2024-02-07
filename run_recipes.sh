#!/bin/bash

. ./admin/bash_utilities.sh

maps=("recipes/maps/map1.yml" "recipes/maps/map2.yml" "recipes/maps/map3.yml" "recipes/maps/map4.yml" "recipes/maps/map5.yml" "recipes/maps/recipe_ocean_quadmap.yml")
transects=("recipes/transects/transect1.yml" "recipes/transects/transect2.yml" "recipes/transects/transect3.yml")
timeseries=("recipes/timeseries/timeseries1.yml" "recipes/timeseries/timeseries2.yml" "recipes/timeseries/timeseries3.yml" "recipes/timeseries/timeseries4.yml" "recipes/timeseries/timeseries5.yml" "recipes/timeseries/timeseries6.yml" "recipes/timeseries/timeseries_atlantic_stream_function.yml" "recipes/timeseries/timeseries_drake.yml")
depths=("recipes/depth_profiles/depth_integration.yml" "recipes/depth_profiles/depth_profile1.yml" "recipes/depth_profiles/depth_profile2.yml")

recipes=( "${maps[@]}" "${transects[@]}" "${timeseries[@]}" "${depths[@]}" )



for recipe in ${recipes[@]};
do
  run_recipe $recipe
done




