import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

q = 1.602*10**(-19)
k = 1.3806*10**(-23)
T = 298
Io = 1*10**(-10) #guess change this later
Rs = 0.001#/243 #guess change this later
Rsh = 10

a = 0.1 #IDK change this later
Vb = -15
m = 3.7

# f(V) = -I + (0.04*15.6*15.6) - Io*np.exp((q*Vint+I*Rs)/(k*T))
# f'(V) = (-Io*q)/(k*T) * np.exp((q*Vint+I*Rs)/(k*T))
###########################################################################################3
#f(V) = -I + (0.04*15.6*15.6) - Io*np.exp((q*Vint+I*Rs)/(k*T)) - ( (Vint+I*Rs)/Rsh )* (1+)
#f'(V) = (-Io*q)/(k*T) * np.exp((q*Vint+I*Rs)/(k*T)) - (1+(a*(1- V+I*Rs)/Vb)**(-m)


# INCLUE A BREAK STATEMENT OFR IF THE VALUES EVER GET TO NEGATIVE (that means way above current 9 or 10, so goes -Inf

Iarray = np.linspace(100,1,num=301)
Varray = np.zeros([301])
for i in range(0,301):
  Vint = 0.7
  error = 10000
  I = Iarray[i]
  while error > 0.0005:
    #Vnew = Vint - ( -I + 0.044*15.6*15.6 - Io*np.exp((q*(Vint+I*Rs)/(k*T)))  ) /  (  (-Io*q)/(k*T) *np.exp((q*(Vint+I*Rs)/(k*T)))  )
    b = (1+0.1 * (1-((Vint+I*Rs)/(-15)))**-3.7)
    Vnew = Vint - ( -I + 0.044*15.6*15.6 - Io*np.exp((q*(Vint+I*Rs)/(k*T))) -((Vint+I*Rs)/Rsh)*b)  /  ((  (-Io*q)/(k*T) *np.exp((q*(Vint+I*Rs)/(k*T)))) - b - 3.7*((0.1*Vint+(I*Rs))/(Rsh*(1+0.1 * (1-(Vint+I*Rs)/(-15))**-4.7))  ))
    error = abs(Vnew-Vint)
    Vint = Vnew #reassign newly calculated value as the new
  Varray[i] = Vint


fig = go.Figure()
fig.add_trace(go.Scatter(x=Varray, y=Iarray,
                    mode='markers',
                    name='markers'))
fig.update_yaxes(range=[-1, 300], dtick=1)
fig.update_xaxes(range=[-18, 0.8], dtick=0.2)

fig.show()
