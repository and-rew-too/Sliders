import numpy as np
import pandas as pd

def array_shader(Ns, Deltashade):
    q = 1.602*10**(-19)
    k = 1.3806*10**(-23)
    T = 298
    Io = 1*10**(-10) #guess change this later
    Rs = 0.001#/243 #guess change this later
    Rsh = 100
    # above is just the intitial constants setup
    
    Iarray3 = np.linspace(15,0.1,num=301)
    Varray = np.zeros([301])
    for i in range(0,301):
        Vint = 0.66*Ns
        error = 10000
        I = Iarray3[i]
        while error > 0.005:
          b = (1+0.1 * (1-((Vint+I*Rs)/(-0.7)))**-3.7)
          Vnew = Vint - ( -I + Deltashade*0.044*15.6*15.6 - Io*np.exp((q*((Vint/Ns)+I*Rs)/(k*T)))  ) / ((  (-Io*q)/(Ns*k*T) *np.exp((q*(Vint/Ns+I*Rs)/(k*T)))) - b - 3.7*((0.1*Vint+(I*Rs))/(Rsh*(1+0.1 * (1-(Vint+I*Rs)/(-0.7))**-4.7))  ))
          
          error = abs(Vnew-Vint)
          Vint = Vnew #reassign newly calculated value as final value
          Varray[i] = Vint
          Varray[i] = -Varray[i]
    return Varray
    # for j in range(300,0,-1):
    #     if np.isinf(V2[j]) == True:
    #         V2[j] = V2[j+1]+(11/301)
    #         Iarray3[j] = Iarray3[j+1]
    #     else:
    #         pass

V3 = array_shader(5, 0.9)
print(V3)



