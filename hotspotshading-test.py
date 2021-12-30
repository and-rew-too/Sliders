import numpy as np
import pandas as pd 

q = 1.62*10**-19
k = 1.38*10**-23
T = 298
Io = 1*10**-10 #guess change this later
Rs = 0.08 #guess change this later
Rsh = 1000 

a = 0.1 #IDK change this later
Vb = -15
m = 3.7

#I = linspace(
#for i in range(1,len(I.index())): 
#  while ,,
#    ...
  
# f(V) = -I + (0.04*15.6*15.6) - Io*np.exp((q*Vint+I*Rs)/(k*T))
# f'(V) = (-Io*q)/(k*T) * np.exp((q*Vint+I*Rs)/(k*T))
###########################################################################################3

#f(V) = -I + (0.04*15.6*15.6) - Io*np.exp((q*Vint+I*Rs)/(k*T)) - ( (Vint+I*Rs)/Rsh )* (1+)
#f'(V) = (-Io*q)/(k*T) * np.exp((q*Vint+I*Rs)/(k*T)) - (1+(a*(1- V+I*Rs)/Vb)**(-m)


# INCLUE A BREAK STATEMENT OFR IF THE VALUES EVER GET TO NEGATIVE (that means way above current 9 or 10, so goes -Inf

# Vint = 0.7
# error = 10000
# while error >= 0.005:
#   #Vnew = Vint - f(Vint)/f'(Vint)
#   Vnew = Vint - ( -I + (0.044*15.6*15.6) - Io*np.exp((q*(Vint+I*Rs)/(k*T)))  ) /  (  (-Io*q)/(k*T) * np.exp((q*(Vint+I*Rs))/(k*T))  )                                                                       
#   error = abs(Vnew-Vint)
  
#   Vint = Vnew #reassign newly calculated value as the new 
#   print(Vint)
Iarray = np.linspace(0,10,num=51)
Varray = pd.Dataframe(np.zeros([1,51]))
for i in range(0,51):
  Vint = 0.7
  error = 10000
  while error > 0.005:
    Vnew = Vint - ( -I + (0.044*15.6*15.6) - Io*np.exp((q*(Vint+I*Rs)/(k*T)))  ) /  (  (-Io*q)/(k*T) * np.exp((q*(Vint+I*Rs))/(k*T))  )    
    error = abs(Vnew-Vint)
    Vint = Vnew #reassign newly calculated value as the new 
  Varray.iloc[0,i] = Vint
print(Varray)
  
  
# fig = go.Figure(data=go.Scatter(x=I, y=Vint))

# fig.update_layout(yaxis_range=[-0.1, 1.5])
# fig.update_layout(
#     title="PV Open Circuit Voltage as a function of Temperature",
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     )
# )

 
  


