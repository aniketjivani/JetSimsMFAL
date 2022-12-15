# import constants and functions for stagnation pressure and temperature
include("./define_constants.jl")

using Printf
using DelimitedFiles

# modify inlet.dat for use in config
# get variable exported from bash
RUN_FOLDER=ENV["RUN_FOLDER"]
NRUNS=parse(Int, ENV["NRUNS"])
RUN_ID=parse(Int, ENV["RUN_ID"])

# use input list in run folder
INPUT_FILE=joinpath(RUN_FOLDER, "input_list.txt")

# load old inlet file data
INLET_FILE_OLD=joinpath(RUN_FOLDER, "run"*@sprintf("%03d", RUN_ID), "inlet.dat")

input_data = readdlm(INPUT_FILE)[:, 5:7] # read scaled up values of uncertain Ue, kappa and nu_tilde

inlet_file_old = readdlm(INLET_FILE_OLD, skipstart=4, header=false)
inlet_data_new = zeros(size(inlet_file_old, 1), size(inlet_file_old, 2))

yy = inlet_file_old[:, 2]
zz = inlet_file_old[:, 3]

inlet_data_new[:, 2] = deepcopy(yy)
inlet_data_new[:, 3] = deepcopy(zz)      
inlet_data_new[:, 6] = ones(size(inlet_file_old, 1)) # nx ny nz = 1 0 0

UCenterline = input_data[RUN_ID, 1]
kappa = input_data[RUN_ID, 2]
nu_tilde = input_data[RUN_ID, 3]

# calculate velocity at each radial location
UeAll = uer(yy, zz, UCenterline, kappa)
MaAll = UeAll ./ aInf # aInf is defined in constants

TStag = T0.(MaAll)
PStag = p0.(MaAll)

inlet_data_new[:, 4] = deepcopy(TStag)
inlet_data_new[:, 5] = deepcopy(PStag)
inlet_data_new[:, 9] = ones(size(inlet_file_old, 1)) * nu_tilde # nu_tilde

# write up new inlet file and overwrite copied one (move temp file to old file path at end)
(tmppath, tmpio) = mktemp()
write(tmpio, "NMARK= 1\n")
write(tmpio, "MARKER_TAG= inlet\n")
write(tmpio, "NROW=1441\n")
write(tmpio, "NCOL=9\n")

write(tmpio, inlet_data_new)

mv(tmppath, INLET_FILE_OLD, force=true)
                            
