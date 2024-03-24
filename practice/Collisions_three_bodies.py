import numpy as np
import random 
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D



def func(x,y):
    return np.pi**2/(1/x+1/y)
# fo = open("test.txt", "w")
k1_max=int(input('请输入k1的上限：'))
k2_max=int(input('请输入k2的上限：'))
#随机选取k_1和k_2的值，电脑性能好的话，可以取更多点
k_1_real=np.array([random.uniform(1,k1_max) for _ in range(0,100)])
k_2_real=np.array([random.uniform(1,k2_max) for _ in range(0,100)])
#保存计算结果
N_real=[]
#带入所有k_1,k_2计算碰撞次数
for k_1,k_2 in zip(k_1_real,k_2_real):
    v_1=-1
    v_2=v_3=0
    cnt=0
    while True:
        if (v_1<0 and v_2-v_1>0) or v_2>v_1:
            v_1,v_2=((k_1-1)*v_1+2*v_2)/(k_1+1),(2*k_1*v_1+(1-k_1)*v_2)/(k_1+1)
            cnt+=1
        if (v_2<0 and v_3-v_2>0) or v_3>v_2:
            v_2,v_3=((k_2-1)*v_2+2*v_3)/(k_2+1),(2*k_2*v_2+(1-k_2)*v_3)/(k_2+1)
            cnt+=1
        if v_3<0:
            v_3=-v_3
            cnt+=1
        if v_1>=0 and v_2>=0 and v_1>=v_2 and v_2>=v_3:
            break
        if (v_2<0 and v_3-v_2>0) or v_3>v_2:
            v_2,v_3=((k_2-1)*v_2+2*v_3)/(k_2+1),(2*k_2*v_2+(1-k_2)*v_3)/(k_2+1)
            cnt+=1
    N_real.append(cnt)

# 定义绘图变量
# fig=plt.figure()
# ax=Axes3D(fig)
# fig.add_axes(ax)
#绘制原始数据散点图
#ax.scatter(k_1_real,k_2_real,N_real,marker='o',color='blue',label='Real')
# #绘制拟合函数的图像


# ax.plot_surface(k_1_real,k_2_real,N_fit,cmap='rainbow',label='Fit')
#设置图例，绘图
# ax.set_xlabel('m1/m2')
# ax.set_ylabel('m2/m3')
# ax.set_zlabel('Number of Collisions')
# plt.grid()
# plt.legend()
# plt.show()




