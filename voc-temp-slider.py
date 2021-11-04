from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd

k = 1.380*10**-23
q = 1.602*10**-19
#ni #intrinsic carrier concentration

#Eg0 = #bandgap extrapolated to zero kelvin (in joules)
#me = #mass of electrons
#mh = #mass of holes
#h = #planck's constant

#4*((2*np.pi*k*T)/h**2)**3 * (me*mh)**(3/2) * np.exp(-Eg0/(k*T))
#ni = B*T**3*np.exp(-Eg0/(k*T))
#B = 4*((2*np.pi*k)/h**2)**3 * (me*mh)**(3/2)
#THIS is where the B constant comes from

T = np.linspace(100, 500, num=400)

#Vg0 = 1.2eV for silicon
#Eg0 = q*Vg0 = 1.2*1.6*10**-19
Vg0 = 1.92*10**-19
gamma = 3
Isc = 0.2
#Voc = ((k*T)/q)*(np.log(Isc)-np.log(B)-gamma*np.log(T)+(q*Vg0)/(k*T))
Voc = ((k*T)/q)*(np.log(Isc)-gamma*np.log(T)+(Vg0)/(k*T))

#simulated Voc for a single junction GaAs cell
Vg2 = 1.42*q
Voc2 = ((k*T)/q)*(np.log(Isc)-gamma*np.log(T)+(Vg2)/(k*T))
#simulated Voc for a Cadmium Telluride thin film
Vg3 = 1.501*q
Voc3 = ((k*T)/q)*(np.log(Isc)-gamma*np.log(T)+(Vg3)/(k*T))


fig = go.Figure(data=go.Scatter(x=T, y=Voc))
fig = make_subplots(rows=1, cols=3, subplot_titles=("Voc v T for c-Si",
                                                    "Voc v T for GaAs",
                                                    "Voc v T for CdTe"))
fig.append_trace(go.Scatter(
        x=T, y=Voc, mode="markers"
        ), row=1, col=1)

fig.append_trace(go.Scatter(
        x=T, y=Voc2, mode="markers"
        ), row=1, col=2)

fig.append_trace(go.Scatter(
        x=T, y=Voc3, mode="markers"
        ), row=1, col=3)

fig.update_layout(yaxis_range=[-0.1, 1.5])
fig.update_layout(
    title="PV Open Circuit Voltage as a function of Temperature",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

#fig.show()
