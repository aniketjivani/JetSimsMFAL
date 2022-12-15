#!/bin/bash                                                                                   

JETDIR=/home/e734/e734/shared/JetSimsMFAL
model=$3 # can be HF or LF!                                                                   
batch=$4

mkdir -p ../runs_${model}_batch_${4}
export RUN_FOLDER=`readlink -f ../runs_${model}_batch_${4}`
export NRUNS=`echo $2 - $1 | bc`

cd ../runs_${model}

for rID in $(seq -f "%03g" $1 $2); do
    # Copies run template folder.
    mkdir run${rID}
    cp ../template_run/inlet.dat run${rID}/inlet.dat
    if [ "$model" == "LF" ]
    then
       cp ../template_run/LoFi_RoundJetG4H.cfg run${rID}/RoundJet_G4H.cfg
    else
	cp ../template_run/HiFi_RoundJetG4H.cfg run${rID}/RoundJet_G4H.cfg
    fi

    julia -e "include("./get_input_list.jl")"
    
    cd run${rID}

    export RUN_ID=${rID}
    julia -e "include("./modify_config.jl")"
    
    # julia -e "include("./range_setup.jl")
    # doModify flag - if doModify is true then only things are rewritten

    # if doModify
    # Modifies the correct run input values.                                                  
    # sh $JETDIR/scripts/modify_inputs.sh ${rID} ${RUNDIR} # check what args need to be given
    # else do nothing
    
    cd ../
done

