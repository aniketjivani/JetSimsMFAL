SHELL=/bin/bash
MODEL=LF
BATCH=256

JETDIR=/work/e734/e734/shared/ajivani/JetSimsMFAL

help:
	@echo "**************************************************************************"
	@echo "In the options above, point to correct directories and software paths "
	@echo "By calling one or more of the targets below, we can generate lists, modify config files"
	@echo "and run multiple SU2 jobs on each of them (hopefully)"
	@echo "every call to generate input list should create a new dir to store all the corresponding"
	@echo "run dirs. The folder name / contents should be descriptive to identify the following: list which was used, subset of runs from list that are to be called with SU2"
	@echo "If computation results are not stored in this folder, point to where they are stored and create a symbolic link for the same"

##############################################################################################
get_julia_mode_emacs:
	chmod +x scripts/getElpa.sh
	./scripts/getElpa.sh

get_list:
	
modify_inlet:
	

run_su2_jobs:
        @echo "@Beckett"

postprocess_all:


clean_test:
	rm -f temp_$(MODEL)
