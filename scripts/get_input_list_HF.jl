using DelimitedFiles
using Random
using Distributions
using ArgParse
using Dates
using LatinHypercubeSampling
using Printf
using DelimitedFiles
# Uncertain inputs:
# 1. Nozzle centerline velocity Ue (velocity profile is top-hat, decays to zero towards wall) - ok with using 293.24 to 312.94 m/s (calculated from rough_calc.jl)
# 2. fraction kappa of nozzle diameter which is momentum thickness (0.1 to 0.3?)
# 3. nu_tilde (orig log MEVR Uniform from 1.53 to 4.6) - convert to nu_tilde
# shell script makes run folders based on arguments for number of runs, model etc 
# Generate input list and accordingly write an inlet.dat file as well for all runs. The master list resides in top level of relevant run folder

mu_l = 1.84592e-5 # N .s / m^2
rhoInf = 0.0722618 # kg / m^3

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
NRUNS = parse(Int, ENV["NRUNS"])

RUN_BATCH = ENV["RUN_BATCH"]

RUN_FOLDER_LF="../runs_LF_batch_" * @sprintf("%02d", parse(Int, RUN_BATCH))

LF_RUNS_SCALED = readdlm(joinpath(RUN_FOLDER_LF, "input_list.txt"))[:, 2:4]


s = ArgParseSettings()
@add_arg_table! s begin
    "--fileLF"
        help = "Path to load LF runs from."
        arg_type = String
    default = "none"

end

args = parse_args(s)

fileLF = args["fileLF"]


# set lower and upper bounds for uncertain parameters (the last value in each is for log MEVR and NOT nu_tilde, that is backed out of samples for log MEVR at the end!!)
lower_bounds = [293.24, 0.1, 1.531]
upper_bounds = [312.94, 0.3, 4.6055]

input_list = zeros(NRUNS, 7) # first column is just run ID, next 3 columns are uniform random betn -1 and +1, last 3 are scaled samples in actual units!

#trunc.(Int, ((ppp2[:, 2] .- old_min) * (new_max - new_min) / (old_max - old_min) .+ new_min))


input_list[:, 1] = collect(1:NRUNS)

LF_RUNS_IDX = zeros(size(LF_RUNS_SCALED, 1), 3)

old_min = -1.0
old_max = 1.0
new_min = 1
new_max = size(LF_RUNS_SCALED, 1)

for i in 1:3
    LF_RUNS_IDX[:, i] = trunc.(Int, ((LF_RUNS_SCALED[:, i] .- old_min) * (new_max - new_min) / (old_max - old_min) .+ new_min))
end

#print(LF_RUNS_IDX)

if fileLF == "none"
    HFPlan, _ = subLHCoptim(LF_RUNS_IDX, NRUNS, 1000)
    HFIdx = sort(subLHCindex(LF_RUNS_IDX, HFPlan))
    print(HFIdx)
else
    HFIdx = readdlm(fileLF, Int, header=false)
end

for (runID, HFID) in enumerate(HFIdx)
    mkdir(joinpath(RUN_FOLDER, @sprintf("run%03d", runID)))
    cp(joinpath(RUN_FOLDER_LF, @sprintf("run%03d", HFID), "example_inlet.dat"), joinpath(RUN_FOLDER, @sprintf("run%03d", runID), "example_inlet_00000.dat"))
    cp(joinpath(RUN_FOLDER_LF, @sprintf("run%03d", HFID), "example_inlet.dat"), joinpath(RUN_FOLDER, @sprintf("run%03d", runID), "example_inlet_00001.dat"))
    cp(joinpath(RUN_FOLDER_LF, @sprintf("run%03d", HFID), "restart_flow.dat"), joinpath(RUN_FOLDER, @sprintf("run%03d", runID), "restart_flow_00000.dat"))
    cp(joinpath(RUN_FOLDER_LF, @sprintf("run%03d", HFID), "restart_flow.dat"), joinpath(RUN_FOLDER, @sprintf("run%03d", runID), "restart_flow_00001.dat"))
end

input_list[:, 2:4] = LF_RUNS_SCALED[HFIdx, :]

# scale back to original quantities using lower and upper bounds
input_list[:, 5] = (1/2) * (upper_bounds[1] - lower_bounds[1]) * input_list[:, 2] .+ (1/2) * (lower_bounds[1] + upper_bounds[1])
input_list[:, 6] = (1/2) * (upper_bounds[2] - lower_bounds[2]) * input_list[:, 3] .+ (1/2) * (upper_bounds[2] + lower_bounds[2])
logMEVR = (1/2) * (upper_bounds[3] -lower_bounds[3]) * input_list[:, 4] .+ (1/2) * (lower_bounds[3] + upper_bounds[3])
input_list[:, 7] = exp.(logMEVR) * (mu_l / rhoInf) # change logMEVR to nu_tilde

    
# write to file
if !isfile(joinpath(RUN_FOLDER, "input_list.txt"))
    open(joinpath(RUN_FOLDER, "input_list.txt"), "w") do io
        writedlm(io, input_list)
    end
else
    # open(joinpath(RUN_FOLDER, "input_list_" * Dates.format(Dates.now(), "yyyy_mm_dd") * ".txt"), "w") do io
    #     writedlm(io, input_list)
    # end# write new file with timestamp appended, and the run folder inlet.dats won't be overwritten UNLESS manually specified to do so. This is to make sure we don't use old results by mistake when we change the inputs for some reason.
end

open(joinpath(RUN_FOLDER, "LF_ID.txt"), "w") do io
    writedlm(io, HFIdx)
end

# copy the restart flow in each LF file to the correct HF folders.
