#!/bin/bash

export RUN_FOLDER_LF=`readlink -f ../runs_LF_batch_0${3}`
export RUN_FOLDER_HF=`readlink -f ../runs_HF_batch_0${3}`
# export PARAM_FILE=`readlink -f $4`

export NRUNS=`echo $2-$1+1 | bc`
export RUN_BATCH=`echo ${3}`


cd $RUN_FOLDER_LF
find -name "flow.vtu" -print | zip -0 ../results_LF_batch_0${3}.zip -@

cd $RUN_FOLDER_HF
find -name "flow_100001.vtu" -print | zip -0 ../results_HF_batch_0${3}.zip -@

cd ../

echo "Zipped LF and LF flow files successfully. End of script"