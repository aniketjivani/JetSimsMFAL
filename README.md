range_setup.sh is the main file for creating all the run folders

Arguments: $1 and $2: starting run ID and ending run ID
$3: LF or HF? depending on that the right config file is supplied
$4: Batch number


Then the script creates the appropriate folders, copies the files and calls Julia scripts that
1. get_input_list.jl: generate input list (this is stored in top level of runs folder)
2. modify_config.jl: modify inlet.dat correctly according to values from input list. Last 3 columns of input list are Uc, kappa and nu_tilde (previous 3 are scaled versions from -1 to +1 for UQ)
