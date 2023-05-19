#!/bin/bash

export RUN_FOLDER_LF=`readlink -f ../runs_LF_batch_0${3}`
export RUN_FOLDER_HF=`readlink -f ../runs_HF_batch_0${3}`
export PARAM_FILE=`readlink -f $4`

export NRUNS=`echo $2-$1+1 | bc`
export RUN_BATCH=`echo ${3}`


# populate HF folders (copy restart files over from LF folders)
cd $RUN_FOLDER_HF

for rID in $(seq -f "%03g" $1 $2); do
    mkdir -p run${rID}
    cd run${rID}
    
    # cp ../../template_run/example_inlet.dat ./example_inlet.dat

    
    cp ../../template_run/HiFi_Transient_RoundJetG4H.cfg ./Transient_RoundJet_G4H.cfg
    cp ../../template_run/HiFi_Avg_RoundJetG4H.cfg ./Avg_RoundJet_G4H.cfg

    cp ${RUN_FOLDER_LF}/run${rID}/example_inlet.dat ./example_inlet_00000.dat
    
    cp ${RUN_FOLDER_LF}/run${rID}/example_inlet.dat ./example_inlet_00001.dat

    cp ${RUN_FOLDER_LF}/run${rID}/example_inlet.dat ./example_inlet_50000.dat
    
    cp ${RUN_FOLDER_LF}/run${rID}/example_inlet.dat ./example_inlet_50001.dat

    cp ${RUN_FOLDER_LF}/run${rID}/restart_flow.dat ./restart_flow_00000.dat

    cp ${RUN_FOLDER_LF}/run${rID}/restart_flow.dat ./restart_flow_00001.dat

    # export RUN_ID=${rID}
    # julia --project=@. ../../scripts/modify_config_HF_batch.jl

    cd ../

done

echo "Folders setup for HF"

# submit HF runs
cd $RUN_FOLDER_HF

for rID in $(seq -f "%03g" $1 $2); do
    start=$(date +%s.%N)
    cd run${rID}
    pwd

	cp ../../template_run/run_job_HF_batch.sbat ./run_job.sbat
    
    echo "Submitting job for run ${rID}"
    sbatch run_job.sbat
    
    cd ../

done