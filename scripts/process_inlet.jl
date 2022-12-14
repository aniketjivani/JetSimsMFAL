using DelimitedFiles
using Printf
using CSV
using DataFrames


inlet_filepath = "../template_run/inlet.dat"


inlet_data = readdlm(inlet_filepath, skipstart=4, header=false)
inlet_df = DataFrame(inlet_data, :auto)
rename!(inlet_df, ["x", "y", "z", "T0", "p0", "nx", "ny", "nz", "nu_tilde"])

rAll = sqrt.(inlet_df.y .^2 + inlet_df.z .^ 2)
#thetaAll = atan.(inlet_df.y ./ inlet_df.z)                                                   

D = 0.06223
Ue(r, Uc, kappa) = Uc * tanh((D/2 - r) / (kappa * D))
