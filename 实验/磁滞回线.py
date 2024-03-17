import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def ja(H, a, b, c,d,e):
    return a * np.arctan(b * (H- c))**e+d


U_H=[-600,-480,-440,-400, -360, -320, -300, -280, -260, -240, -222, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 567]

U_B=[-241, -227, -220, -207, -194, -175, -149, -125, -75, -44, 0, 26, 60, 92, 116, 133, 144, 156, 168, 178, 183, 188, 193, 200, 206, 210, 213, 216, 232]

H_1=list(map(lambda x:(150/(0.13*2.5))*0.001*x,U_H))
B_1=list(map(lambda x:(0.03/(150*1.24*0.0001)*x*0.001),U_B))


H_2=list(map(lambda x:-x-0.01,H_1))
B_2=list(map(lambda x:-x-0.01,B_1))

H_1=H_1+H_2
B_1=B_1+B_2

H1=[round(H_i,0) for H_i in H_1]
H1=list(map(lambda x:int(x),H1))
print(H1)
B1=[round(B_i,3) for B_i in B_1]
B1=list(map(lambda x:int(x*1000),B1))
print(B1)
Point_H=[-102.48,103.61,-276.88,276.93,0,0]
Point_B=[0,0,-0.3886,0.3788,0.232,-0.2425]
plt.rc('font',family='Times New Roman',size=14)
plt.title('Hysteresis Loop')
plt.plot(H_1,B_1,c='b',label='Hysteresis Loop')
#plt.scatter(H_1,B_1,marker='x',c='r')
plt.scatter(Point_H,Point_B,c='k',marker='^')
plt.text(-20,0.25,"$B_r$",size=14)
plt.text(0,-0.26,"$-B_r$",size=14)
plt.text(-101.48,0,'$-H_c$',size=14)
plt.text(105.61,0,'$H_c$',size=14)
plt.text(276.93,0.3788,'$(H_m,B_m)$',size=14)
plt.text(-380,-0.3286,'$(-H_m,-B_m)$',size=14)
plt.xlim(-400,400)
plt.xlabel('H(A/m)')
plt.ylabel('B(T)')
plt.grid()
plt.legend()
plt.show()




