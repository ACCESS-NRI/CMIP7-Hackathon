#!/bin/bash

pbs_job=$(cat <<-END
#!/bin/bash -l 
#PBS -S /bin/bash
#PBS -P iq82
#PBS -l storage=gdata/fs38+gdata/oi10+gdata/rr3+gdata/xp65+gdata/al33+gdata/rt52+gdata/zz93+scratch/nf33+gdata/ct11
#PBS -l wd
#PBS -q normal
#PBS -l walltime=04:00:00
#PBS -l mem=64GB
#PBS -l ncpus=1

module use /g/data/xp65/public/modules
module load esmvaltool

esmvaltool run --output_dir=/scratch/nf33/\$USER/esmvaltool_outputs \$recipe

END

)

function run_recipe(){

	recipe=$1

	if test -f $recipe; then
	    qsub -v recipe=$recipe -N$(basename -- $recipe .yml) -e admin/logs/$(basename -- $recipe .yml).stderr -o admin/logs/$(basename -- $recipe .yml).stdout <<<"$pbs_job"
            echo "Running recipe: $recipe"
	else
	    echo "$recipe does not exist, please check the path."
	fi

}
