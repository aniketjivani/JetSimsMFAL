#!/bin/bash                                                                                   

model=$3
batch=$4

export RUN_FOLDER=`readlink -f ../runs_${model}_batch_${4}`

cd $RUN_FOLDER

for rID in $(seq $1 $2); do
    start=$(date +%s.%N)
    cd run${rID}

    cp ../../template_run/run_job.sbat ./run_job.sbat

    sbatch run_job.sbat
    
    cd ../
    duration=$(echo "$(date +%s.%N) - $start" |bc)
    execution_time=`printf "%.5f seconds " $duration`
    file_out=./output.out
    if [ ! -f "$file_out" ] ;
    then
        touch $file_out
    fi
    echo "Run ${rID} completed in ${execution_time}" >&1 | tee -a $file_out
done
