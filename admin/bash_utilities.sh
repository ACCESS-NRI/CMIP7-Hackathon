#!/bin/bash

pbs_job=$(cat <<-END
#!/bin/bash -l 
#PBS -S /bin/bash
#PBS -P iq82
#PBS -l storage=gdata/kj13+gdata/fs38+gdata/oi10+gdata/rr3+gdata/xp65+gdata/al33+gdata/rt52+gdata/zz93+scratch/tm70
#PBS -W umask=037
#PBS -l wd
#PBS -q normal
#PBS -l walltime=04:00:00
#PBS -l mem=64GB
#PBS -l ncpus=12

module use /g/data/xp65/public/modules
module load esmvaltool

esmvaltool run --max_parallel_tasks=1 --output_dir=/scratch/tm70/rb5533/esmvaltool_outputs \$recipe

END

)

function run_recipe(){

	recipe=$1
	if test -f $recipe; then
	    qsub -v recipe=$recipe -N$(basename -- $recipe .yml) -e admin/logs/$(basename -- $recipe .yml).stderr -o admin/logs/$(basename -- $recipe .yml).stdout <<<"$pbs_job"
        else
            echo $recipe does not exist, please check the path
	fi

}
