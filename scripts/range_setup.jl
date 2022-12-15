using DelimitedFiles
using Random
using Distributions
using ArgParse
using Dates

# Uncertain inputs:
# 1. Nozzle centerline velocity Ue (velocity profile is top-hat, decays to zero towards wall) - ok with using 293.24 to 312.94 m/s (calculated from rough_calc.jl)
# 2. fraction kappa of nozzle diameter which is momentum thickness (0.1 to 0.3?)
# 3. nu_tilde (orig log MEVR Uniform from 1.53 to 4.6) - convert to nu_tilde
# shell script makes run folders based on arguments for number of runs, model etc 
# Generate input list and accordingly write an inlet.dat file as well for all runs. The master list resides in top level of relevant run folder



# SHELL script
# JETDIR=/home/e734/e734/shared/JetSimsMFAL
# model=$3 # can be HF or LF!                                                                      

# mkdir -p ../runs_${model}
# cd ../runs_${model}

# for rID in $(seq -f "%03g" $1 $2); do
#     # Copies run template folder.                                                                
#     cp -r ../template_run run${rID}
#     cd run${rID}

#     # Modifies the correct run input values.                                                     
#     sh $JETDIR/scripts/modify_inputs.sh ${rID}

#     cd ../
# done

# shell will export some variables like name of run folder and number of runs, & we will make use of those directly.


RUN_FOLDER = ENV["RUN_FOLDER"]
NRUNS = ENV["NRUNS"]

p0∗ = 10218.4466 # nominal value around which we varied stagnation pressure in old runs.

# set lower and upper bounds for uncertain parameters (the last value in each is for MEVR and NOT nu_tilde, that is backed out of samples for MEVR at the end!!)
lower_bounds = [293.24, 0.1, 4.6228]
upper_bounds = [312.94, 0.3, 100.036]

input_list = zeros(NRUNS, 7) # first column is just run ID, next 3 columns are uniform random betn -1 and +1, last 3 are scaled samples in actual units!

input_list[:, 1] = collect(1:NRUNS)

input_list[:, 2] = rand(Uniform(-1, 1), NRUNS)
input_list[:, 3] = rand(Uniform(-1, 1), NRUNS)
input_list[:, 4] = rand(Uniform(-1, 1), NRUNS)

# scale back to original quantities using lower and upper bounds
input_list[:, 5] = (1/2) * (upper_bounds[1] - lower_bounds[1]) * input_list[:, 2] + (1/2) * (lower_bounds[1] + upper_bounds[1])
input_list[:, 6] = (1/2) * (upper_bounds[2] - lower_bounds[2]) * input_list[:, 3] + (1/2) * (upper_bounds[2] + lower_bounds[2])
input_list[:, 7] = (1/2) * (log(upper_bounds[3]) -log(lower_bounds[3])) * input_list[:, 4] + (1/2) * (log(lower_bounds[3]) + log(upper_bounds[3]))


# write to file
if !isfile(joinpath(RUN_FOLDER, "input_list.txt"))
    open(joinpath(RUN_FOLDER, "input_list.txt"), "w") do io
        writedlm(input_list)
    end
else
    open(joinpath(RUN_FOLDER, "input_list_" * Dates.format(Dates.now(), "yyyy_mm_dd") * ".txt"))# write new file with timestamp appended, and the run folder inlet.dats won't be overwritten UNLESS manually specified to do so. This is to make sure we don't use old results by mistake when we change the inputs for some reason.
end


# pass correct variables back to the shell for further processing



# check values for p0 based on p0∗ and ensure they are in roughly the right range.
