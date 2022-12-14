SHELL=/bin/bash
MODEL=LF


help:
	@echo "**************************************************************************"
	@echo "In the options above, point to correct directories and software paths "
	@echo "By calling one or more of the targets below, we can generate lists, modify config files"
	@echo "and run multiple SU2 jobs on each of them (hopefully)"
	@echo "every call to generate input list should create a new dir to store all the corresponding"
	@echo "run dirs. The folder name / contents should be descriptive to identify the following: list which was used, subset of runs from list that are to be called with SU2"
	@echo "If computation results are not stored in this folder, point to where they are stored and create a symbolic link for the same"

##############################################################################################


generate_input_list:
	
modify_config_files:
	

run_su2_jobs:
        @echo "@Beckett"

postprocess_all:


clean_test:
	rm -f temp_$(MODEL)
