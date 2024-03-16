import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
#定义常量
a=1.378e+5
b=0.03183
R=8.1344622e+3
#临界值
T_c=8*a/(27*R*b)
V_c=3*b
P_c=a/(27*b*b)
#定义Vander Waals方程
def Van_P(V,T):
    return (R*T/(V-b)-a/(V*V))*0.00001
#定义求解极值点函数
def Extreme(T):
    coeff=[1,-2*a/(R*T),4*a*b/(R*T),-2*a*b*b/(R*T)]
    V_root=np.roots(coeff)
    V_root=list(sorted(V_root))
    V_m,V_M=V_root[1],V_root[2]
    return V_m,V_M,Van_P(V_m,T),Van_P(V_M,T)
#定义求解积分域函数
def scope(P,T):
    coeff=[1,-(b+R*T/(P*1e5)),a/(P*1e5),-a*b/(P*1e5)]
    V_root=np.roots(coeff)
    V_root=list(sorted(V_root))
    return V_root[0],V_root[1],V_root[2]
#储存数据列表
V_m_list=[]
V_M_list=[]
P_m_list=[]
P_M_list=[]
V_L=[]
V_R=[]
P_equ=[]
T_list=[]
for i in range(1,500):
    T=T_c-i*0.1
    T_list.append(T)
    #极值点计算与储存
    V_m,V_M,P_m,P_M=Extreme(T)
    V_m_list.append(V_m)
    V_M_list.append(V_M)
    P_m_list.append(P_m)
    P_M_list.append(P_M)    
    #使用迭代法求解
    P_mid=(P_m+P_M)/2
    func=lambda V:P_mid-Van_P(V,T)
    while True:
        if P_mid>0:
            V_left,V_mid,V_right=scope(P_mid,T)
            integral_1,error_1=quad(func,V_left,V_mid)
            integral_2,error_2=quad(func,V_mid,V_right)
            s=integral_1+integral_2
            if np.abs(s)<0.0001:
                V_L.append(V_left)
                V_R.append(V_right)
                break
            if s>0:
                P_mid,P_M=(P_m+P_mid)/2,P_mid
            else:
                P_mid,p_m=(P_M+P_mid)/2,P_mid
        else:
            P_m=0
            P_mid=P_M/2      
    P_equ.append(Van_P(V_left,T))

plt.rc('font',family='Times New Roman',size=14)
fig = plt.figure(figsize=(14, 6))
axs = fig.subplots(nrows=1, ncols=2)
#绘制不同T下的Vander Waals方程的P-V曲线
V_van=np.linspace(1*b,10*b,500)
for t in range(0,4):
    T_van=T_c-t*10+10
    if t==1:
        axs[0].plot(V_van,Van_P(V_van,T_van),c='k',label='$T_c$')
    else:
        axs[0].plot(V_van,Van_P(V_van,T_van),c='c')
#绘制Binodal line
V_L.reverse()
V_total=V_L+V_R
P_total=P_equ.copy()
P_total.reverse()
P_total=P_total+P_equ
axs[0].plot(V_total,P_total,linestyle='--',c='r',label='Binodal')
#绘制Spinodal line
V_m_list.reverse()
V_list=V_m_list+V_M_list
P_m_list.reverse()
P_list=P_m_list+P_M_list
axs[0].plot(V_list,P_list,linestyle=':',c='b',label='Spinodal')
#设置子图1参数
axs[0].plot(V_c,P_c/100000,'bo',label='Critical Point')
axs[0].text(V_c-0.018,P_c/100000+1.5,'$(P_c,V_c)$')
axs[0].set_title("Binodal and Spinodal")
axs[0].set_xlabel('V(L/mol)')
axs[0].set_ylabel("P(bar)")
axs[0].set_ylim(0,80)
axs[0].set_xlim(0.03,0.35)
axs[0].legend()
axs[0].grid()
#绘制P-T相图
axs[1].plot(T_list,P_equ,'k',label='Phase Equilibrium')
axs[1].plot(T_c,P_c/100000,'bo',label='Critical Point')
axs[1].text(T_c-3,P_c/100000+2,'$(P_c,T_c)$')
axs[1].text(120,50,'Liquid',size=22)
axs[1].text(150,15,'Gas',size=22)
axs[1].set_title('P-T Phase Diagram')
axs[1].set_xlabel('T(K)')
axs[1].set_ylabel('P(bar)')
axs[1].set_xlim(100,170)
axs[1].set_ylim(0,70)
axs[1].legend()
axs[1].grid()
plt.show()