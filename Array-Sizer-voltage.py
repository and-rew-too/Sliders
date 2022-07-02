import pandas as pd
import numpy as np
import math


celltech = "silicon"  # either silicon, gaas, cdte, cigs
NOCT = 323  # Kelvin, needed to determine temperature derating, 323 is NOCT
Pdesired = 78  # Watts, total power
Vdesired = 18  # Volts, voltage
wsh = 0.4  # assumption is that shingle gap is 4mm
LengthTotal = 67.7 #677cm is the length for lri






if "silicon" in celltech:
    Vmp = 0.650
    beta = -.0020
    alpha = .00038
elif "gaas" in celltech:
    Vmp = 0.747  # estimate
    beta = -.0014
    alpha = .00070
elif "cdte" in celltech:
    Vmp = 0.697  # estimate
    beta = -.0028
    alpha = .00040
elif "cigs" in celltech:
    Vmp = 0.720  # estimate
    beta = -.003
    alpha = .0001
else:
    print("double check spelling plz")
    exit()
# Jsc of advanced hjt silicon 0.042 A/cm2
# Jsc of topcon silicon ~0.038-0.04 A/cm2
# Jsc of gaas 0.022 A/cm2
# Jsc of cdte 0.026 A/cm2
# Jsc of cigs 0.026 A/cm2
Vd = 0.75 #voltage drop over diode
Vw = 0.75 #voltage drop due to resistivity of length of wiring / jbox
Vdesired = Vdesired + (1*(1.38*10**-23)*NOCT) / \
                       (1.602*10**-19) * np.log(800/1000)
Ns = (Vdesired + Vd + Vw) / ((Vmp)*(1+beta*(NOCT-273)))
FinalLength = 15.8
FinalWidth = LengthTotal/Ns + wsh

Idesired = Pdesired / Vdesired #find current requirement from Power and Voltage
Imp = 0.95*(0.04*15.8*(FinalWidth-wsh)) #the 0.95 is generally ratio of Isc:Imp
Np = Idesired / ((Imp)*(1+alpha*(NOCT-273))*(800/1000)*(1-0.002*20))

print("number series: {}, number parallel: {}".format(Ns, Np))
print("real number series:{}, real number parallel: {}".format(
    math.ceil(Ns), math.ceil(Np)))
print("Shingle width:{}, Shingle length *constant: {}".format(
    FinalWidth, FinalLength))


