# Rough calculations to back out Uc and kappa ranges.                                         

# M(pStag, gamma; pInf=6223)=sqrt((2/(gamma-1)) * (exp(-((gamma-1)/gamma) * log(pInf/pStag)) - 1))

γ = 1.4
TInf=300
pInf=6223
RAir = 287.87

T0(ma) = TInf * (1 + ((γ - 1)/2) * ma^2)

p0(ma) = pInf * (1 + ((γ - 1)/2) * ma^2)^(γ/(γ - 1))


function uer(yData, zData, UeC, kappa)
    rData = sqrt.(yData.^2 + zData .^2)
    UeData = []
    for r in rData
        push!(UeData, UeC * tanh(((1/2) - r)/(kappa)))
    end
    return UeData
end


aInf = sqrt(γ * TInf * RAir)

println("Freestream sound speed = ", aInf, " m/s")

mu_l = 1.84592e-5 # N.s/m^2
rhoInf = 0.0722618 # kg / m^3

nu_l = mu_l / rhoInf

# MLower = M(0.97 * 10218.44, 1.4)
# MUpper = M(1.03 * 10218.44, 1.4)

# ueUpper = MLower * aInf
# ueLower = MUpper * aInf


