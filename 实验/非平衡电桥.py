import numpy as np
import matplotlib.pyplot as plt 

plt.rc('font',family='Times New Roman',size=14)

# t_1=[32,36.8,40.5,46,51.1,56.3,60,65.5]
# t=[x-22.6 for x in t_1]
# U_0=[11.3,17.1,21.5,27.8,33.6,39.4,43.5,49.5]
# y=[4*54.85*x*0.001/(50*(1.3-2*x*0.001))*100 for x in U_0]
# print(t)
# y_1=[round(x,4) for x in y]
# print(y_1)
# coef,cov=np.polyfit(t,y_1,deg=1,cov=True)
# corr=np.corrcoef(t,y)
# func=np.poly1d(coef)
# x_fit=[x for x in range(5,50)]
# y_fit=func(x_fit)
# print(coef)
# print(corr[0,1])
# print(np.sqrt(np.diag(cov)))
# plt.scatter(t,y,marker='x',c='r',label='Original Date')
# plt.plot(x_fit,y_fit,c='b',label='Fit line')
# plt.title('Nonequilibrium')
# plt.xlabel('$t-t_0(\mathrm{^oC})$')
# plt.ylabel('$10^{-2}$')
# plt.legend()
# plt.grid()
# plt.show()

t_2=[31,35.7,40.5,45.3,50.1,54.7,60,65]
R=[57,58,59,60,61,62.04,63.14,64.23]
coef,cov=np.polyfit(t_2,R,deg=1,cov=True)
corr=np.corrcoef(t_2,R)
print(coef[0]/coef[1])
print(corr[0,1])
print(np.sqrt(np.diag(cov)))
func=np.poly1d(coef)
x=[x for x in range(25,70)]
y=func(x)
plt.scatter(t_2,R,marker='x',c='r',label='Original Date')
plt.plot(x,y,c='b',label='Fit line')
plt.xlabel('$\mathrm{t/^oC}$')
plt.ylabel('$\mathrm{R/\Omega}$')
plt.title("Equilibrium")
plt.legend()
plt.grid()
plt.show()
