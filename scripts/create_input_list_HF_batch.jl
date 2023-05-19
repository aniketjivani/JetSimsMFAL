using DelimitedFiles
using Random
using Distributions
using ArgParse
using Dates
using Printf

mu_l = 1.84592e-5 # N .s / m^2
rhoInf = 0.0722618 # kg / m^3


RUN_FOLDER_LF = ENV["RUN_FOLDER_LF"]
RUN_FOLDER_HF = ENV["RUN_FOLDER_HF"]
NRUNS = parse(Int, ENV["NRUNS"])

RUN_BATCH = ENV["RUN_BATCH"]

s = ArgParseSettings()
@add_arg_table! s begin
    "--fileParam"
        help = "Path to load parameters from for new batch."
        arg_type = String
    default = "none"
end

args = parse_args(s)

fileParam = args["fileParam"]

# set lower and upper bounds for uncertain parameters (the last value in each is for log MEVR and NOT nu_tilde, that is backed out of samples for log MEVR at the end!!)
lower_bounds = [293.24, 0.1, 1.531]
upper_bounds = [312.94, 0.3, 4.6055]

input_list = zeros(NRUNS, 7) # first column is just run ID, next 3 columns are uniform random betn -1 and +1, last 3 are scaled samples in actual units!

input_list[:, 1] = collect(1:NRUNS)
input_list[:, 2:4] = readdlm(fileParam)

# scale back to original quantities using lower and upper bounds
input_list[:, 5] = (1/2) * (upper_bounds[1] - lower_bounds[1]) * input_list[:, 2] .+ (1/2) * (lower_bounds[1] + upper_bounds[1])
input_list[:, 6] = (1/2) * (upper_bounds[2] - lower_bounds[2]) * input_list[:, 3] .+ (1/2) * (upper_bounds[2] + lower_bounds[2])
logMEVR = (1/2) * (upper_bounds[3] -lower_bounds[3]) * input_list[:, 4] .+ (1/2) * (lower_bounds[3] + upper_bounds[3])
input_list[:, 7] = exp.(logMEVR) * (mu_l / rhoInf) # change logMEVR to nu_tilde


if !isfile(joinpath(RUN_FOLDER_LF, "input_list.txt"))
    open(joinpath(RUN_FOLDER_LF, "input_list.txt"), "w") do io
        writedlm(io, input_list)
    end
end

if !isfile(joinpath(RUN_FOLDER_HF, "input_list.txt"))
    open(joinpath(RUN_FOLDER_HF, "input_list.txt"), "w") do io
        writedlm(io, input_list)
    end
end


