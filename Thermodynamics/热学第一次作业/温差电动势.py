import matplotlib.pyplot as plt
import numpy as np

alpha=0.21
beta=-1e-4

def epsi(t):
    return alpha*t+beta*t*t

def t_a(e):
    return 5*e

fig=plt.figure(figsize=(17,5))
axs=fig.subplots(nrows=1,ncols=3)
t=np.linspace(-100,500,500)

t1=t_a(epsi(t))
plt.rc('font',family='Times New Roman',size=12)
axs[2].plot(t1,t)
axs[2].set_title('$t-t^*$')
axs[2].set_xlabel('$t*/^o$')
axs[2].set_ylabel('$t/^oC$')
axs[2].legend()
axs[2].grid()


temp=t

epsilon=epsi(temp)

axs[0].plot(temp,epsilon,label='Thermoelectric EMF')
axs[0].set_title('Thermoelectric EMF - Temperature')
axs[0].set_xlabel('t/$^o$C')
axs[0].set_ylabel('EMF/mV')
axs[0].legend()
axs[0].grid()


epsilon=np.linspace(-22,80,500)
t_b=list(map(lambda e:e*5,epsilon))

axs[1].plot(t_b,epsilon,label='Thermoelectric EMF')
axs[1].set_title('Thermoelectric EMF -New Temperature')
axs[1].set_xlabel('t$^*/^o$')
axs[1].set_ylabel('EMF/mV')
axs[1].legend()
axs[1].grid()
plt.show()
