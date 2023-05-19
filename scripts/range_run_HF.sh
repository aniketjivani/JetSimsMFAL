#!/bin/bash                                                                                   

model=$3
batch=$4

export RUN_FOLDER=`readlink -f ../runs_${model}_batch_${4}`

cd $RUN_FOLDER

for rID in $(seq -f "%03g" $1 $2); do
    start=$(date +%s.%N)
    cd run${rID}
    pwd
    if [ "$model" == "LF" ]
    then
	cp ../../template_run/run_job_LF.sbat ./run_job.sbat
    else
	cp ../../template_run/run_job_HF.sbat ./run_job.sbat
    fi
    
    sbatch run_job.sbat
    
    cd ../

done
