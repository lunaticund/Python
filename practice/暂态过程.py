import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(t,a):
    return 5*(1-np.exp(-t/a))

t=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1.2]
V=[1.1,1.9,2.5,3,3.5,3.8,4.1,4.4,4.7]

coef,pcov=curve_fit(func,t,V)

print(coef)
fig,axes=plt.subplots()
y_ticks = np.linspace(0, 5, 11)
x_ticks = np.linspace(0, 2, 11)

plt.scatter(t,V,c='b',marker='x',label='Origin')
t1=np.linspace(0,2,300)
plt.plot(t1,func(t1,coef),c='r',label='Fit')
plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['Times New Roman']
plt.title('Capacitor Charging Process',fontsize=17)
plt.xlabel('t/ms',fontsize=15)
plt.ylabel('U/V',fontsize=15)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.legend()

axes.set_xticks(x_ticks)
axes.set_yticks(y_ticks)


plt.grid()
plt.show()