import pandas as pd
import numpy as np
import math


celltech = "silicon" #either enter silicon, gaas, cdte, cigs
NOTC = 323 #needed to determine actual temperatures, if not, will make assumption of a mounted panel at 323K
Pdesired = 80 #W
Idesired = 4.3 #A
wsh = 0.5 #assumption is that shingle gap is 5mm

if "silicon" in celltech:
    Vmp = 0.560
    beta = -.0020
    alpha = .00038
elif "gaas" in celltech:
    Vmp = 0.747 #estimate
    beta = -.0014
    alpha = .00070
elif "cdte" in celltech:
    Vmp = 0.697 #estimate
    beta = -.0028
    alpha = .00040
elif "cigs" in celltech:
    Vmp = 0.720 #estimate
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
Isc = 0.040*15.8*(2.6-wsh)
Imp = 0.95*Isc
print(Imp)
Np = Idesired / ( (Imp)*(1+alpha*(NOTC-273))*(800/1000)*(1-0.002*20)  )
#f1 is a polynomial relation to wsh so like a*wsh**3 + b*wh**2 + c*wh**1
#Np = .... / .... * f1


Vl = Pdesired/Idesired
print(Vl)
Vd = 0.75
Vw = 0.75

Ns = (Vl + Vd + Vw) / ( (Vmp)*(1+beta*(NOTC-273)))



print("number series: {}, number parallel: {}".format(Ns, Np))
print("real number series:{}, real number parallel: {}".format( math.ceil(Ns), math.ceil(Np)) )






#future add-ons
#include an angling of the panel, so have the angle between normal and AOI (whether flat, 1-axis tracker, 2-axis tracker)
#include a degradation rate that accounts for the degree 
#include choice for years needed to operate, currently hard set at 20 years
#include voc dependence upon the illumination amount Voc(S')
#include cell technology option for peroskites expected around 2025 2030(since started in 2014)

#include a double check of proper sizing with cell efficiency and final power given the total cell area
#include a ^ packing factor of brickwork to determine overall module size in final layout 
