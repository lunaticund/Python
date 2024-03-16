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

plt.plot(H_1,B_1,c='b')
plt.scatter(H_1,B_1,marker='x',c='r')
plt.grid()
plt.legend()
plt.show()




