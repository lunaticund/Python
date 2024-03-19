import numpy as np
import matplotlib.pyplot as plt

#测量电阻率
# R=(6.641,6.644,6.652,6.654,6.653,6.651)
# print(np.mean(R))
# R_eps=np.std(R,ddof=1)/np.sqrt(len(R))
# print(R_eps)
# d=(4.22,4.12,4.10,4.18,4.12,4.10)
# print(np.mean(d))
# d_eps=np.std(d,ddof=1)/np.sqrt(len(d))
# print(d_eps)

plt.rc('font',family='Times New Roman',size=14)
fig = plt.figure(figsize=(12,5))
axs = fig.subplots(nrows=1, ncols=2)
#升温
t_up=(30,35.1,41.9,45.9,50.7,55.2,60.4,65.1)
R_up=(4.871,4.984,5.104,5.18,5.262,5.347,5.445,5.535)
coeff_up,cov=np.polyfit(t_up,R_up,deg=1,cov=True)
corr_up=np.corrcoef(t_up,R_up)
# print(np.sqrt(np.diag(cov)))
# print(coeff_up)
# print(coeff_up[0]/coeff_up[1]*100000)
# print(corr_up[0,1])
func_up=lambda x:coeff_up[0]*x+coeff_up[1]

# R1=tuple(R-func_up(t) for R,t in zip(R_up,t_up))
# s_y=np.sqrt(sum(map(lambda x:x**2,R1))/(len(R1)-2))
# print(s_y)
# u_b=s_y/np.sqrt(np.var(t_up))
# print(u_b)
# u_a=u_b*np.sqrt(sum(map(lambda x:x**2,t_up))/len(t_up))
# print(u_a)


t_up_fit=np.linspace(25,70,300)
R_up_fit=func_up(t_up_fit)
axs[0].plot(t_up_fit,R_up_fit,c='b',label='Fit line')
axs[0].scatter(t_up,R_up,marker='^',c='r',label='Origin data')
axs[0].grid()
axs[0].legend()
axs[0].set_title('R-t at Rising Temperature')
axs[0].set_xlabel('$t(^oC)$')
axs[0].set_ylabel('$R(10^{-3}\Omega)$')

#降温
t_down=(32.8,38.1,43.4,48.8,54.2,59.7)
R_down=(4.950,5.050,5.150,5.250,5.350,5.450)
coeff_down,cov=np.polyfit(t_down,R_down,deg=1,cov=True)
corr_down=np.corrcoef(t_down,R_down)
print(coeff_down)
print(np.sqrt(np.diag(cov)))
print(coeff_down[0]/coeff_down[1]*100000)
print(corr_down[0,1])
func_down=lambda x:coeff_down[0]*x+coeff_down[1]



t_down_fit=np.linspace(25,70,300)
R_down_fit=func_down(t_up_fit)
axs[1].plot(t_down_fit,R_down_fit,c='b',label='Fit line')
axs[1].scatter(t_down,R_down,marker='s',c='r',label='Origin data')
axs[1].grid()
axs[1].legend()
axs[1].set_title('R-t at Drpping Temperature')
axs[1].set_xlabel('$t(^oC)$')
axs[1].set_ylabel('$R(10^{-3}\Omega)$')
plt.show()