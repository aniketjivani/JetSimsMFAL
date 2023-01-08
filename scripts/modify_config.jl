# import constants and functions for stagnation pressure and temperature
include("./define_constants.jl")

using Printf
using DelimitedFiles

# modify inlet.dat for use in config
# get variable exported from bash
RUN_FOLDER=ENV["RUN_FOLDER"]
# NRUNS=parse(Int, ENV["NRUNS"])
RUN_ID=parse(Int, ENV["RUN_ID"])

RUN_BATCH=ENV["RUN_BATCH"]

# use input list in run folder
INPUT_FILE=joinpath(RUN_FOLDER, "input_list.txt")

# name of copied inlet file from template_run, should be example_inlet with extra points
INLET_FILE_OLD=joinpath(RUN_FOLDER, "run"*@sprintf("%03d", RUN_ID), "example_inlet.dat")

# get values of UCenterline, kappa and nu_tilde
input_data = readdlm(INPUT_FILE, header=false)[:, 5:7]


# if RUN_BATCH == "test"
#     UCenterline = input_data[1, 1]
#     kappa = input_data[1, 2]
#     nu_tilde = input_data[1, 3]
# else
    UCenterline = input_data[RUN_ID, 1] # RUN ID is redundant if we are running a test case - always 1 run
    kappa = input_data[RUN_ID, 2]
    nu_tilde = input_data[RUN_ID, 3]
# end

# read y and z coordinates from inlet file
inlet_data = readdlm(INLET_FILE_OLD, skipstart=5, header=false)
yy = inlet_data[:, 2]
zz = inlet_data[:, 3]

# Calculate the stagnation pressure and temperature based on top hat velocity profile
UeAll = uer(yy, zz, UCenterline, kappa)
MaAll = UeAll ./ aInf # aInf is defined in constants

TStag = T0.(MaAll)
PStag = p0.(MaAll)

# Move velocity, temperature, pressure and nu_tilde to a new temp file
open("./ue_t0_p0_nu_tilde.txt", "w") do io
    write(io, "NMARK= 1\n")
    write(io, "MARKER_TAG= inlet\n")
    write(io, "NROW=1505\n")
    write(io, "NCOL=4\n")
    write(io, "#UE TEMPERATURE PRESSURE NU_TILDE\n")
    writedlm(io, [UeAll TStag PStag ones(length(yy)) * nu_tilde])
end

inlet_data_new = zeros(size(inlet_data, 1), size(inlet_data, 2))

inlet_data_new[:, 2] = deepcopy(yy)
inlet_data_new[:, 3] = deepcopy(zz)      
inlet_data_new[:, 6] = ones(size(inlet_data, 1)) # nx ny nz = 1 0 0
inlet_data_new[:, 4] = deepcopy(TStag)
inlet_data_new[:, 5] = deepcopy(PStag)
inlet_data_new[:, 9] = ones(size(inlet_data, 1)) * nu_tilde # nu_tilde

# write up new inlet file and overwrite copied one (move temp file to old file path at end)
(tmppath, tmpio) = mktemp()
write(tmpio, "NMARK= 1\n")
write(tmpio, "MARKER_TAG= inlet\n")
write(tmpio, "NROW=1505\n")
write(tmpio, "NCOL=9\n")

flush(tmpio)

mv(tmppath, INLET_FILE_OLD, force=true)

open(INLET_FILE_OLD, "a") do io
    writedlm(io, inlet_data_new)
end
