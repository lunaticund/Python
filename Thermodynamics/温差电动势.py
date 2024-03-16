import matplotlib.pyplot as plt
import numpy as np

alpha=0.21
beta=-1e-4

def epsi(t):
    return alpha*t+beta*t*t

def t_a(e):
    return 5*e

t=np.linspace(-100,500,500)

t1=t_a(epsi(t))
plt.rc('font',family='Times New Roman',size=12)
plt.plot(t1,t)
plt.title('$t-t^*$')
plt.xlabel('$t*/^o$')
plt.ylabel('$t/^oC$')
plt.legend()
plt.grid()
plt.show()

# temp=np.linspace(-100,500,500)

# epsilon=epsi(temp)
# plt.rc('font',family='Times New Roman',size=12)
# plt.plot(temp,epsilon,label='Thermoelectric EMF')
# plt.title('Thermoelectric EMF - Temperature')
# plt.xlabel('t/$^o$C')
# plt.ylabel('EMF/mV')
# plt.legend()
# plt.grid()
# plt.show()

# epsilon=np.linspace(-22,80,500)
# t_b=list(map(lambda e:e*5,epsilon))
# plt.rc('font',family='Times New Roman',size=12)
# plt.plot(t_b,epsilon,label='Thermoelectric EMF')
# plt.title('Thermoelectric EMF -New Temperature')
# plt.xlabel('t$^*/^o$')
# plt.ylabel('EMF/mV')
# plt.legend()
# plt.grid()
# plt.show()
