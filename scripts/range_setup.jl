using DelimitedFiles
using Random
using Distributions


# Uncertain inputs:
# 1. Nozzle centerline velocity Ue (velocity profile is top-hat, decays to zero towards wall) - ok with using 293.24 to 312.94 m/s (calculated from rough_calc.jl)
# 2. fraction kappa of nozzle diameter which is momentum thickness (0.1 to 0.3?)
# 3. nu_tilde (orig log MEVR Uniform from 1.53 to 4.6) - convert to nu_tilde
# based on arguments for number of runs, model etc 
# Generate input list and accordingly write an inlet.dat file as well for all runs



