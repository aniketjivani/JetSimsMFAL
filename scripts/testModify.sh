Pressure_val=`awk -v rid=${run_ID} 'NR==rid {print $3}' ../inputs_reference_list_Mach_pressur\
e.txt`
sed 's/PRESSURE_HOLDER/'${Pressure_val}'/' testingAwk.cfg > testingAwk_2.cfg
