#!/bin/bash                                                                                   

cd runs

for rID in $(seq $1 $2); do
    start=$(date +%s.%N)
    cd wdir.${rID}

    # Runs SU2.                                                                               
    mpirun -n 4 SU2_CFD RoundJet_G4H.cfg > screen.out
    #SU2_CFD input.cfg > screen.out                                                           
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
