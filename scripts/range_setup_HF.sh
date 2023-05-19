#!/bin/bash                                                                                   

JETDIR=readlink -f ../
model="HF"                                                                   
batch=$4

mkdir -p ../runs_${model}_batch_${4}
export RUN_FOLDER=`readlink -f ../runs_${model}_batch_${4}`
export NRUNS=`echo $2-$1+1 | bc`
export RUN_BATCH=`echo ${4}`

cd $RUN_FOLDER

julia --project=@. ../scripts/get_input_list_HF.jl --fileLF=/work/e734/e734/shared/ajivani/JetSimsMFAL/old_cfg_runs_HF_batch_01/LF_ID.txt


cd $RUN_FOLDER
for rID in $(seq -f "%03g" $1 $2); do
    # Copies run template folder.
    # mkdir run${rID}
    cd run${rID}

    
    cp ../../template_run/HiFi_Transient_RoundJetG4H.cfg ./Transient_RoundJet_G4H.cfg
    cp ../../template_run/HiFi_Avg_RoundJetG4H.cfg ./Avg_RoundJet_G4H.cfg


    # cd run${rID}

    #export RUN_ID=${rID}
    #julia --project=@. ../../scripts/modify_config.jl # creates a temp file of temperature pressure and nu_tilde

    cd ../
done
#fi
