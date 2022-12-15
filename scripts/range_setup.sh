#!/bin/bash                                                                                   

JETDIR=/work/e734/e734/shared/ajivani/JetSimsMFAL
model=$3 # can be HF or LF!                                                                   
batch=$4

mkdir -p ../runs_${model}_batch_${4}
export RUN_FOLDER=`readlink -f ../runs_${model}_batch_${4}`
export NRUNS=`echo $2-$1+1 | bc`

cd $RUN_FOLDER

for rID in $(seq -f "%03g" $1 $2); do
    # Copies run template folder.
    mkdir run${rID}
    cd run${rID}
    cp ../../template_run/inlet.dat ./inlet.dat
    if [ "$model" == "LF" ]
    then
       cp ../../template_run/LoFi_RoundJetG4H.cfg ./RoundJet_G4H.cfg
    else
       cp ../../template_run/HiFi_RoundJetG4H.cfg ./RoundJet_G4H.cfg
    fi

    julia ../../scripts/get_input_list.jl
    
    # cd run${rID}

    export RUN_ID=${rID}
    julia ../../scripts/modify_config.jl
    
    
    cd ../
done

