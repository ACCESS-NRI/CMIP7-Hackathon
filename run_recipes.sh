#!/bin/bash

maps=("recipes/maps/map1.yml" "recipes/maps/map2.yml" "recipes/maps/map3.yml" "recipes/maps/map4.yml" "recipes/maps/map5.yml")
transects=("recipes/transects/transect1.yml" "recipes/transects/transect2.yml" "recipes/transects/transect3.yml")
timeseries=("recipes/timeseries/timeseries1.yml" "recipes/timeseries/timeseries2.yml" "recipes/timeseries/timeseries3.yml" "recipes/timeseries/timeseries4.yml" "recipes/timeseries/timeseries5.yml" "recipes/timeseries/timeseries6.yml")
depths=("recipes/depth_profiles/depth_integration.yml" "recipes/depth_profiles/depth_profile1.yml" "recipes/depth_profiles/depth_profile2.yml")

models=( "${maps[@]}" "${transects[@]}" "${timeseries[@]}" "${depths[@]}" )


for model in ${models[@]};
do
	qsub -v script=$model -N$(basename -- $model .yml) -e admin/logs/$(basename -- $model .yml).stderr -o admin/logs/$(basename -- $model .yml).stdout  job.pbs
done




