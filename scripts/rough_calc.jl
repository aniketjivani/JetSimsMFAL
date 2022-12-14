# Rough calculations to back out Uc and kappa ranges.                                         

# Basic steps:                                                                                
# 1. Start with values of p0 range we used in old paper: 0.97, 1.03 x p0.                     
# 2. Using this and isentropic relation for pressure with gamma=1.4, calculate upper and lower bounds of Jet Mach number (make sure it doesn't go supersonic)
# 3. Now using calculated Mach number, get temperature range with isentropic relation and freestream = 300 K                                                                               
# 4. Back out Ue using local speed of sound                                                   
# 5. Now play with different Uc and kappa combinations that satisfy Uc. plot profiles see what would make a good range.
# 6. Try upper and lower bound of the ranges (2-4 runs), see how much variation we have. Use RANS with modified inlet file and check if we are producing right flow output files or not. If not, what changes do we need?                                                               

M(pStag, gamma; pInf=6223)=sqrt((2/(gamma-1)) * (exp(-((gamma-1)/gamma) * log(pInf/pStag)) - 1))



TStag(ma, gamma; tInf=300) = tInf * (1 + ((gamma - 1)/2) * ma^2)

gamma_val = 1.4
TInf=300
RAir = 287.87

aInf = sqrt(gamma_val * TInf * RAir)

println("Freestream sound speed = ", aInf, " m/s")


MLower = M(0.97 * 10218.44, 1.4)
MUpper = M(1.03 * 10218.44, 1.4)

ueUpper = MLower * aInf
ueLower = MUpper * aInf


