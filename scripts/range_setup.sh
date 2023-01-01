#!/bin/bash                                                                                   

JETDIR=readlink -f ../
model=$3 # can be HF or LF!                                                                   
batch=$4

mkdir -p ../runs_${model}_batch_${4}
export RUN_FOLDER=`readlink -f ../runs_${model}_batch_${4}`
export NRUNS=`echo $2-$1+1 | bc`
export RUN_BATCH=`echo ${4}`

cd $RUN_FOLDER

if [ "$batch" == "test" ]
then
    mkdir run001
    cd run001
    cp ../../template_run/example_inlet.dat ./example_inlet.dat
    if [ "$model" == "LF" ]
    then
	cp ../../template_run/LoFi_RoundJetG4H_modified_options.cfg ./RoundJet_G4H.cfg
    else
	cp ../../template_run/HiFi_RoundJetG4H.cfg ./RoundJet_G4H.cfg
    fi

    julia --project=@. ../../scripts/get_input_list.jl	   
    
    export RUN_ID=1
    julia --project=@. ../../scripts/modify_config.jl # creates a temp file of temperature pressure and nu_tilde
    cd ../
    
else
    for rID in $(seq -f "%03g" $1 $2); do
	# Copies run template folder.
	mkdir run${rID}
	cd run${rID}
	cp ../../template_run/example_inlet.dat ./example_inlet.dat
	if [ "$model" == "LF" ]
	then
	    cp ../../template_run/LoFi_RoundJetG4H_modified_options.cfg ./RoundJet_G4H.cfg
	else
	    cp ../../template_run/HiFi_RoundJetG4H.cfg ./RoundJet_G4H.cfg
	fi
	
	julia --project=@. ../../scripts/get_input_list.jl	   
	
	# cd run${rID}

	export RUN_ID=${rID}
	julia --project=@. ../../scripts/modify_config.jl # creates a temp file of temperature pressure and nu_tilde
	
	cd ../
    done
fi


