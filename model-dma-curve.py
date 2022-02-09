import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = pd.DataFrame(np.logspace(-14.0, 9.0, num=200))

y = pd.DataFrame(np.zeros(len(x.index)))
y = y + 5.07 #G0

G = pd.DataFrame([1.01,
2.51,5.99,14.48,28.72,46.02,66.85,
84.26,94.18,99.13,101.69,102.88,104.27,
101.95])
tau = pd.DataFrame([2760000,
184000,18600,
2340,318,
40.7,4.23,
0.372,0.0258,
0.00124,0.0000368,
0.000000867,0.000000017,
0.00000000038])
for i in range(0,13):
    #print(G.loc[i])
    for j in range(0,len(x.index)): #G1-13
        y.loc[j] = y.loc[j] + G.loc[i]*np.exp(-x.loc[j]/tau.loc[i])


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=[7, 11])
ax1.plot(x.loc[:], y.loc[:], ':b', linewidth=2, label='G = G0 + summation (G_i * exp(-t/tau_i)')
ax1.set_title('Exponential plot', fontsize=15)
ax1.set_xlabel('x-axis', fontsize=13)
ax1.set_ylabel('y-axis', fontsize=13)
ax1.legend()

ax2.loglog(x.loc[:],y.loc[:], '--r', linewidth=2, label='e ^ (2.3 * x + 3.7)')
ax2.set_title('loglog exponential plot', fontsize=15)
ax2.set_xlabel('log(x)', fontsize=13)
ax2.set_ylabel('log(y)', fontsize=13)
ax2.legend()

plt.ylim([1, 1000])
plt.tight_layout()
plt.show()
exit()
