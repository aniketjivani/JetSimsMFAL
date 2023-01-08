#!/bin/bash                                                                                   

model=$3
batch=$4

export RUN_FOLDER=`readlink -f ../runs_${model}_batch_${4}`

cd $RUN_FOLDER

for rID in $(seq -f "%03g" $1 $2); do
    start=$(date +%s.%N)
    cd run${rID}
    pwd
    cp ../../template_run/run_job.sbat ./

    sbatch run_job.sbat
    
    cd ../

done
