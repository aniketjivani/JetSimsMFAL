#!/bin/bash

# arguments 1 and 2 are number of runs. 
# argument 3 is batch number
# argument 4 is filepath for new param list.

# make HF and LF folders
JETDIR=readlink -f ../
# model="HF"                                                                 
batch=$3

mkdir -p ../runs_LF_batch_0${3}
mkdir -p ../runs_HF_batch_0${3}

export RUN_FOLDER_LF=`readlink -f ../runs_LF_batch_0${3}`
export RUN_FOLDER_HF=`readlink -f ../runs_HF_batch_0${3}`
export PARAM_FILE=`readlink -f $4`

export NRUNS=`echo $2-$1+1 | bc`
export RUN_BATCH=`echo ${3}`


# take in list as argument (julia script) - copy created param list to both HF and LF run folders!
julia --project=@. ../scripts/create_input_list_HF_batch.jl --fileParam=${PARAM_FILE}

echo "Input list created"

cd $RUN_FOLDER_LF

# populate LF folders
for rID in $(seq -f "%03g" $1 $2); do
    mkdir -p run${rID}
	cd run${rID}
    cp ../../template_run/example_inlet.dat ./example_inlet.dat
    cp ../../template_run/LoFi_RoundJetG4H.cfg ./RoundJet_G4H.cfg

    export RUN_ID=${rID}
    julia --project=@. ../../scripts/modify_config_HF_batch.jl # modify inlet files and creates a temp file of temperature pressure and nu_tilde

    cd ../
done

echo "Inlet files modified"

# submit LF runs
cd $RUN_FOLDER_LF

for rID in $(seq -f "%03g" $1 $2); do
    start=$(date +%s.%N)
    cd run${rID}
    pwd
	cp ../../template_run/run_job_LF.sbat ./run_job.sbat
    
    echo "Submitting job for run ${rID}"
    sbatch run_job.sbat
    
    cd ../
done


# # populate HF folders (copy restart files over from LF folders)
# cd $RUN_FOLDER_HF

# for rID in $(seq -f "%03g" $1 $2); do
#     mkdir -p run${rID}
#     cd run${rID}
    
#     # cp ../../template_run/example_inlet.dat ./example_inlet.dat

    
#     cp ../../template_run/HiFi_Transient_RoundJetG4H.cfg ./Transient_RoundJet_G4H.cfg
#     cp ../../template_run/HiFi_Avg_RoundJetG4H.cfg ./Avg_RoundJet_G4H.cfg

#     cp ${RUN_FOLDER_LF}/run${rID}/example_inlet.dat ./example_inlet_00000.dat
    
#     cp ${RUN_FOLDER_LF}/run${rID}/example_inlet.dat ./example_inlet_00001.dat

#     cp ${RUN_FOLDER_LF}/run${rID}/example_inlet.dat ./example_inlet_50000.dat
    
#     cp ${RUN_FOLDER_LF}/run${rID}/example_inlet.dat ./example_inlet_50001.dat

#     cp ${RUN_FOLDER_LF}/run${rID}/restart_flow.dat ./restart_flow_00000.dat

#     cp ${RUN_FOLDER_LF}/run${rID}/restart_flow.dat ./restart_flow_00001.dat

#     # export RUN_ID=${rID}
#     # julia --project=@. ../../scripts/modify_config_HF_batch.jl

#     cd ../

# done

# echo "Folders setup for HF"

# # submit HF runs
# cd $RUN_FOLDER_HF

# for rID in $(seq -f "%03g" $1 $2); do
#     start=$(date +%s.%N)
#     cd run${rID}
#     pwd

# 	cp ../../template_run/run_job_HF_batch.sbat ./run_job.sbat
    
#     echo "Submitting job for run ${rID}"
#     sbatch run_job.sbat
    
#     cd ../

# done


# # # zip LF and HF flow files, put in main JetSimsMFAL directory.
# # cd $RUN_FOLDER_LF
# # find -name "flow.vtu" -print | zip -0 ../results_LF_batch_${3}.zip -@

# # cd $RUN_FOLDER_HF
# # find -name "flow_100001.vtu" -print | zip -0 ../results_HF_batch_${3}.zip -@

# # cd ../

# # echo "Zipped LF and LF flow files successfully. End of script"

