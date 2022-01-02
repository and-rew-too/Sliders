from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pandas as pd


import math
from scipy.optimize import curve_fit
Length = 80 #cm
Width = 48 #cm
Area = Length*Width

sheet_url = "https://docs.google.com/spreadsheets/d/12RYFtjew1XxsE4Tf3L7E2ABPJv7y6wk80gXFf52WVzU/edit#gid=0"
pd.set_option('display.width', None)

url_1 = sheet_url.replace('/edit#gid=' , '/export?format=csv&gid=')
df = pd.read_csv(url_1,)
print(df)
def objective(x, a, c):
	return a*(x**-1.286) + c
    # b was actually the x^n power had to enter manually to find a solution
    # find it here, in desmos link https://www.desmos.com/calculator/og5tjbyujk

x = df.iloc[:,1]
y = df.iloc[:,10]
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, c = popt
# interploting values from 15 mm to 160mm and plotting the new curve
x_new = np.linspace(15, 75, 121)
y_new = objective(x_new, a, c)
Vmp = 0.7* (y_new/100 *(1-(1.05*0.038/0.7) ) / 0.95 )

####### above is alll old shit from the other array-sizer problem, shows Voc degrades as cell width decreases




#https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/35-eupvsec-2018/Mondon_5BO93.pdf
#ODD RESULTS: as you chnage the 
# do not account for the increased shading/cell and assume voc always the same (WILL VOC STILL BE CONSTANT AS wsh increases??) 
# do not account for changing resistive losses as shingle width changes
# do not account for ?? 
####### now is where the new, newer code starts
DIVB = 121
Isc = np.zeros([DIVB])
Ns = np.zeros([DIVB])
V = np.zeros([DIVB])
wsh = np.linspace(1.5,7.5,DIVB)
deadspace = np.zeros([DIVB])

for i in range(0,DIVB):
    Ns[i] = math.floor(Length/(wsh[i]-0.6)) #assumption of 6mm overlap
    V[i] = Ns[i]*Vmp[i]
    #print(wsh[i])
    Isc[i] = (0.044*Width*(wsh[i]-0.6)) #ALSO ASSUMING entire module width is full of cells, doesnt factor in gaps placed in between cells in the horizontal direction, when placed in rows
    deadspace[i] = Length - Ns[i]*(wsh[i]-0.6) 
print(Isc)
Power = 0.9*Isc*V



fig = go.Figure()
fig.add_trace(go.Scatter(x=wsh, y=Power,
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=wsh, y=Isc,
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=wsh, y=V,
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=deadspace, y=V,
                    mode='markers',
                    name='markers'))


fig.show()

exit()
