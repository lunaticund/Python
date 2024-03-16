import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def func(x,a2,a3,a4,a5,a6):
    return a2*x**4+a3*x**3+a4*x**2+a5*x+a6

def divde(x,y):
    return y/x

U_H=[23.8,57.3,88,120.2,148,167,218.5,250,290,406,563,803]
U_B=[21,51,81.2,110.5,135.2,149.8,174.5,187,197.5,218.5,232,244]

# U_H=[23.8,57.3,88,110.2,120.2,131.2,148,167,172.5,218.5,250,290,406,563,803]
# U_B=[21,51,81.2,101.2,110.5,119.8,135.2,149.8,156,174.5,187,197.5,218.5,232,244]
H=list(map(lambda x:(150/(0.13*2.5))*0.001*x,U_H))
B=list(map(lambda x:1000*(0.03/(150*1.24*0.0001)*x*0.001),U_B))

mu=[]
for H_i,B_i in zip(H,B):
    mu.append(B_i/H_i)

coef=np.polyfit(H,mu,deg=4)

H_fit=np.linspace(10,300,500)
mu_fit=func(H_fit,*coef)

plt.plot(H_fit,mu_fit,c='b',label='Fit Line')
plt.scatter(H[:-1],mu[:-1],marker='x',color='r',label='Original Datas')
plt.rc('font',family='Times New Roman',size=12)
plt.title('$\mu-H$')
plt.xlabel('H(A/m)')
plt.ylabel('$\mu( 10^{-3}(N/A^2))$')
plt.grid()
plt.legend()
plt.show()