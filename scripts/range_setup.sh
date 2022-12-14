#!/bin/bash                                                                                   

JETDIR=/home/e734/e734/shared/JetSimsMFAL
model=$3 # can be HF or LF!                                                                   

mkdir -p ../runs_${model}
cd ../runs_${model}

for rID in $(seq -f "%03g" $1 $2); do
    # Copies run template folder.                                                             
    cp -r ../template_run run${rID}
    cd run${rID}

    # Modifies the correct run input values.                                                  
    sh $JETDIR/scripts/modify_inputs.sh ${rID}

    cd ../
done
