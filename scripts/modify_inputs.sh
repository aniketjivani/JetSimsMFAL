#!/bin/bash                                                                                   

run_ID=$1

PRESSURE_VALUE=`awk -v rid=$run_ID 'NR==rid {print $3}' ../../old_input_list_2020.txt`
sed 's/PRESSURE_HOLDER/'${PRESSURE_VALUE}'/g' RoundJet_G4H.cfg > RoundJet_G4H2.cfg
rm -f RoundJet_G4H.cfg
mv RoundJet_G4H2.cfg RoundJet_G4H.cfg
