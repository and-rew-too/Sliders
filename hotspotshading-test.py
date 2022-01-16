import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def find_nearest(array, value):
    array = np.nan_to_num(array)
    idx = (np.abs(array - value)).argmin()
    #return array[idx]
    return idx

q = 1.602*10**(-19)
k = 1.3806*10**(-23)
T = 298
Io = 1*10**(-10) #guess change this later
Rs = 0.001#/243 #guess change this later
Rsh = 100

Ns = 20
a = 0.1 #IDK change this later
Vb = -15
m = 3.7
#imagine a standard 60 cell array with 3 bypass diodes
# Iarray/Varray is the shaded array
# V1 is the 'unshaded' first string of 20 cells
# V2 is the 'unshaded' second string of 20 cells
# V3 is the 'unshded' third string of 20 cells
Iarray = np.linspace(200,1,num=301)
Varray = np.zeros([301])
for i in range(0,301):
  Vint = 0.66
  error = 10000
  I = Iarray[i]
  #SHADING PERCENT
  deltaS = 0.7
  while error > 0.0005:
    #Vnew = Vint - ( -I + 0.044*15.6*15.6 - Io*np.exp((q*(Vint+I*Rs)/(k*T)))  ) /  (  (-Io*q)/(k*T) *np.exp((q*(Vint+I*Rs)/(k*T)))  )
    b = (1+0.1 * (1-((Vint+I*Rs)/(Vb)))**-3.7)
    Vnew = Vint - ( -I + deltaS*0.044*15.6*15.6 - Io*np.exp((q*(Vint+I*Rs)/(k*T))) -((Vint+I*Rs)/Rsh)*b)  /  ((  (-Io*q)/(k*T) *np.exp((q*(Vint+I*Rs)/(k*T)))) - b - 3.7*((0.1*Vint+(I*Rs))/(Rsh*(1+0.1 * (1-(Vint+I*Rs)/(Vb))**-4.7))  ))
    error = abs(Vnew-Vint)
    Vint = Vnew #reassign newly calculated value as the new
  Varray[i] = Vint

#finding the index at which all those values are getting skipped through
Vmax = np.zeros([301])
for i in range(1,301):
    Vmax[i] = Varray[i]-Varray[i-1]
df = pd.DataFrame(Vmax, columns = ['Vmax'])
column = df["Vmax"]
A = column.idxmax()
#now appending OPTIONAL
Vadd = np.linspace(Varray[A]-column.max(),Varray[A],num=90)
Varray = np.append(Varray,Vadd)
IAdd = np.zeros([90])+Iarray[A]
Iarray = np.append(Iarray,IAdd)
#print(Iarray)





Iarray1 = np.linspace(15,0.1,num=301)
V1 = np.zeros([301])
for i in range(0,301):
  Vint = 0.66*Ns
  error = 10000
  I = Iarray1[i]
  while error > 0.005:
    #Vnew = 0.66*6 - ( -I + 0.044*15.6*15.6 - Io*np.exp((q*(0.11+I*Rs)/(k*T)))  ) /  (  (-Io*q)/(k*T*6) *np.exp((q*(0.11+I*Rs)/(k*T)))  )
    #error = abs(Vnew-0.66*6)
    Vnew = Vint - ( -I + 0.044*15.6*15.6 - Io*np.exp((q*((Vint/Ns)+I*Rs)/(k*T)))  ) /  (  (-Io*q)/(Ns*k*T) *np.exp((q*((Vint/Ns)+I*Rs)/(k*T)))  )
    error = abs(Vnew-Vint)
    Vint = Vnew #reassign newly calculated value as the new
    V1[i] = Vint
    V1[i] = -V1[i]
print(V1)


#WHAT THIS DOES IS at the overflow point, where I increases so dramatically,
#that is the Isc --> Imp region replace all (exponential) NaN values there with the Imp point essentially
# NEED isnan for diode with b values
# NEED isinf for diode without b value, just standard diode model
# for i in range(300,0,-1):
#     if np.isinf(V1[i]) == True:
#         V1[i] = V1[i+1]+(11/301)
#         Iarray1[i] = Iarray1[i+1]
#     else:
#         pass





from numpy import inf
Varray = np.nan_to_num(Varray)
Varray[Varray == 0] = inf
#V1 already has infinity values?

df = pd.DataFrame(np.zeros([301,200]))
for i in range(0,301):
    for j in range(0,200):
        dist = abs(Varray[i]-V1[j])+abs(Iarray[i]-Iarray1[j])
        df.iloc[i,j] = dist
A = df.stack().idxmin()
#A is a 1x2 tuple containing the row and the column of values
#HARD CODE, best values are 108 and also 287
print(type(df.stack().idxmin()))

print(V1[A[1]])
print(Varray[A[0]])
Pdisappate = -Varray[287]*Iarray[287]
#diodePdisappate = Varray[287]*(Isc-Iarray[287])
print(Pdisappate)
exit()
#############################################################################
#THE ABOVE is the first half, during which the single diode is overlapped with
#the (-x) V2 array to find the operating point, while down below
#second half is appending all values into a single IV curve at 2 appropriate points


Iarray2 = np.linspace(15,0.1,num=301)
V2 = np.zeros([301])
for i in range(0,301):
  Vint = 0.66*Ns
  error = 10000
  I = Iarray2[i]
  while error > 0.0005:
    #Vnew = Vint - ( -I + 0.044*15.6*15.6 - Io*np.exp((q*(Vint+I*Rs)/(k*T)))  ) /  (  (-Io*q)/(k*T) *np.exp((q*(Vint+I*Rs)/(k*T)))  )
    #b = (1+0.1 * (1-((Vint+I*Rs)/(-0.7)))**-3.7)
    #Vnew = Vint - ( -I + 0.2*0.044*15.6*15.6 - Io*np.exp((q*(Vint+I*Rs)/(k*T))) -((Vint+I*Rs)/Rsh)*b)  /  ((  (-Io*q)/(k*T) *np.exp((q*(Vint+I*Rs)/(k*T)))) )
    Vnew = Vint - ( -I + 0.5*0.044*15.6*15.6 - Io*np.exp((q*((Vint/Ns)+I*Rs)/(k*T)))  ) / ((  (-Io*q)/(Ns*k*T) *np.exp((q*(Vint/Ns+I*Rs)/(k*T)))) - b - 3.7*((0.1*Vint+(I*Rs))/(Rsh*(1+0.1 * (1-(Vint+I*Rs)/(-0.7))**-4.7))  ))
    if Vnew > 1000000:
        pass
    error = abs(Vnew-Vint)
    #print(error)
    Vint = Vnew #reassign newly calculated value as the new
    V2[i] = Vint
    V2[i] = -V2[i]
#WHAT THIS DOES IS at the overflow point, where I increases so dramatically,
#that is the Isc --> Imp region replace all (exponential) NaN values there with the Imp point essentially
for j in range(300,0,-1):
    if np.isinf(V2[j]) == True:
        V2[j] = V2[j+1]+(11/301)
        Iarray2[j] = Iarray2[j+1]
    else:
        pass

Iarray3 = np.linspace(15,0.1,num=301)
V3 = np.zeros([301])
for i in range(0,301):
  Vint = 0.66*Ns
  error = 10000
  I = Iarray3[i]
  while error > 0.0005:
    #Vnew = Vint - ( -I + 0.044*15.6*15.6 - Io*np.exp((q*(Vint+I*Rs)/(k*T)))  ) /  (  (-Io*q)/(k*T) *np.exp((q*(Vint+I*Rs)/(k*T)))  )
    b = (1+0.1 * (1-((Vint+I*Rs)/(-0.7)))**-3.7)
    #Vnew = Vint - ( -I + 0.2*0.044*15.6*15.6 - Io*np.exp((q*(Vint+I*Rs)/(k*T))) -((Vint+I*Rs)/Rsh)*b)  /  ((  (-Io*q)/(k*T) *np.exp((q*(Vint+I*Rs)/(k*T)))) )
    Vnew = Vint - ( -I + 0.8*0.044*15.6*15.6 - Io*np.exp((q*((Vint/Ns)+I*Rs)/(k*T)))  ) / ((  (-Io*q)/(Ns*k*T) *np.exp((q*(Vint/Ns+I*Rs)/(k*T)))) - b - 3.7*((0.1*Vint+(I*Rs))/(Rsh*(1+0.1 * (1-(Vint+I*Rs)/(-0.7))**-4.7))  ))
    if Vnew > 1000000:
        pass
    error = abs(Vnew-Vint)
    Vint = Vnew
    V3[i] = Vint
    V3[i] = -V3[i]
#WHAT THIS DOES IS at the overflow point, where I increases so dramatically,
#that is the Isc --> Imp region replace all (exponential) NaN values there with the Imp point essentially
for j in range(300,0,-1):
    if np.isinf(V2[j]) == True:
        V2[j] = V2[j+1]+(11/301)
        Iarray3[j] = Iarray3[j+1]
    else:
        pass
#################################################################################
# FINDS where the string V3 begins to diverge, that's the Vmp and then
# splice the strings together into a single large IV curve with summed voltage
V3 = -V3
V1 = -V1
V2 = -V2

# NUMBER AT voltage.. AT WHICH TO SPLICE
# below is now appending V3 to V1, 2 out of 3 done
Vsp = 13
Splice = find_nearest(V1, Vsp)
print(find_nearest(V1, Vsp))
V3 = V3 + Vsp + 0.7 # THE VALUE of the bypass diode
V1 = np.append(V1[0:Splice],V3)
Iarray1 = np.append(Iarray1[0:Splice],Iarray3)

# below is now appending V2 TO V1+V3 combined, 3 out of 3 done
Splice = find_nearest(V1, Vsp*2)
print(find_nearest(V1, Vsp*2))
V2 = V2 + Vsp*2 + 0.7 # THE VALUE of the bypass diode
V1 = np.append(V1[0:Splice],V2)
Iarray1 = np.append(Iarray1[0:Splice],Iarray2)


###############################################################################
fig = go.Figure()
# fig.add_trace(go.Scatter(x=V2, y=Iarray2,
#                      mode='markers',
#                      name='markers'))
fig.add_trace(go.Scatter(x=V1, y=Iarray1,
                    mode='markers',
                    name='markers'))
#fig.add_trace(go.Scatter(x=Varray, y=Iarray,
#                    mode='markers',
#                    name='markers'))

fig.add_shape(type='line',
                x0=50, y0=0, x1=-20, y1=0,
                line={'dash': 'dash', 'color': 'red'},
                xref='x',
                yref='y')
fig.add_shape(type='line',
                x0=0, y0=15, x1=0, y1=0,
                line={'dash': 'dash', 'color': 'red'},
                xref='x',
                yref='y')
fig.show()
# f(V) = -I + (0.04*15.6*15.6) - Io*np.exp((q*Vint+I*Rs)/(k*T))
# f'(V) = (-Io*q)/(k*T) * np.exp((q*Vint+I*Rs)/(k*T))
###########################################################################################3
#f(V) = -I + (0.04*15.6*15.6) - Io*np.exp((q*Vint+I*Rs)/(k*T)) - ( (Vint+I*Rs)/Rsh )* (1+)
#f'(V) = (-Io*q)/(k*T) * np.exp((q*Vint+I*Rs)/(k*T)) - (1+(a*(1- V+I*Rs)/Vb)**(-m)
