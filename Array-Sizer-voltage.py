import pandas as pd
import numpy as np
import math


celltech = "silicon"  # either enter silicon, gaas, cdte, cigs
NOTC = 323  # K needed to determine actual temperatures, if not, will make assumption of a mounted panel at 323K
Pdesired = 108  # W
Vdesired = 30  # V
wsh = 0.5  # assumption is that shingle gap is 5mm

if "silicon" in celltech:
    Vmp = 0.650  # resistive losses drive that vmp value
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
    print("error: double check spelling plz")
    exit()
# Jsc of advanced heterojunction silicon 0.042 A/cm2
# Jsc of semi-advanced topcon silicon ~0.038-0.04 A/cm2
# Jsc of gaas 0.022 A/cm2
# Jsc of cdte 0.026 A/cm2
# Jsc of cigs 0.026 A/cm2
Vd = 0.75
Vw = 0.75  # may be a bit high

#NEW vmp, adjust for illumination
Vdesired = Vdesired + (1*(1.38*10**-23)*NOTC) / \
                       (1.602*10**-19) * np.log(800/1000)
Ns = (Vdesired + Vd + Vw) / ((Vmp)*(1+beta*(NOTC-273)))

Il = Pdesired / Vdesired
#Isc = 0.040*15.8*(2.6-wsh)
Imp = 0.95*(0.04*15.8*(2.6-wsh))
#print(Imp)
Np = Il / ((Imp)*(1+alpha*(NOTC-273))*(800/1000)*(1-0.002*20))
#f1 is a polynomial relation to wsh so like a*wsh**3 + b*wh**2 + c*wh**1
#Np = .... / .... * f1


print("number series: {}, number parallel: {}".format(Ns, Np))
print("real number series:{}, real number parallel: {}".format(
    math.ceil(Ns), math.ceil(Np)))

