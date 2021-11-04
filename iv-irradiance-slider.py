import plotly.graph_objects as go
import numpy as np
import pandas as pd

q = 1.60217662 * (10**(-19))  # elementary charge
k = 1.38064852 * (10**(-23))  # Boltzmanns constant
n = 1.4  # ideality factor
I_SC = 6.15
V_OC = 0.721
T = 298.15  # Cell temperature
V = np.linspace(0.0, V_OC+0.05, num=50)  # using voltage as input variable
T_0 = 298.15  # reference temp = 25C
I_r0 = 1000  # reference Irradiance
TC = 0.0029  # temp coefficint of Isc by manufacturer
V_g = 1.79*(10**(-19))  # band gap in joules

#Imesh, Vmesh = np.meshgrid(np.linspace(200, 1000, 20), V)
I_r = 1000  # irradiance input
I_s0 = 1.2799*(10**(-8))  # saturation current at ref temp
#OFTEN marked as I0, saturation current and ideality factor n of a cell are indicators of quality of the Cell
#I_s0 = q*A*((D*Ni**2) / (L*Nd))
#A is cell area
#D is minority carrier diffusivity (so boron or phosphorus)
#L is minority carrier diffusion length
#Nd is doping
#ni is intrinsic carrier concentration for silicon (a constant)
# intrinsic carrier concentration HUGE equation... kinda long

# for a in range(10):
#     I_ph = ((I_SC/I_r0).*Irradiance).*(1 + TC*(T-T_0))
#     # saturation current eq
#     I_s = = I_s0 .* (T./T_0). ^ (3/n) .* exp((-(q.*V_g)/n*k).*((1./T)-(1/T_0)))
#     # final voltage-current equation
#     I = I_ph - I_s .*exp(((q.*V_mesh[a]) / (n*k*T)-1))

I_ph = ((I_SC/I_r0)*200)*(1 + TC*(T-T_0))
I_s = I_s0**(T/T_0)**(3/n) * np.exp((-(q*V_g)/n*k)*((1/T)-(1/T_0)))
I = I_ph - I_s * np.exp(((q*V) / (n*k*T)-1))

fig = go.Figure(data=go.Scatter(x=V, y=I))

fig.update_layout(yaxis_range=[0, 1.5])
fig.update_layout(
    title="Plot Title",
    xaxis_title="Current (I)",
    yaxis_title="Voltage (V)",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
fig.update_annotations(font_size=12)


fig.show()

