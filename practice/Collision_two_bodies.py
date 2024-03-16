import numpy as np
import matplotlib.pyplot as plt

#定义猜想的函数形式
def func_fit(x):
    return np.sqrt(x)*np.pi

k_max=int(input('请输入k的最大取值:'))
y_real=[]
#在0到n之间随机选取
x=list(np.linspace(0,k_max,500))
#对所有的x，算出碰撞次数
for k in x:
    u=-1
    v=cnt=0
    while True:
        u,v=((k-1)*u+2*v)/(k+1),(2*k*u+(1-k)*v)/(k+1)
        cnt+=1
        if v<0:
            v=-v
            cnt+=1
        if u>0 and (np.abs(v)<u):
            break
    y_real.append(cnt)
#绘制图像,其中真实数据为蓝色散点，拟合的函数为红色亮线
plt.scatter(x,y_real,marker='.',color='blue',label='Real')
plt.plot(x,func_fit(x),color='red',label='Fit')
plt.xlabel('M/m')
plt.ylabel('Number of Collisions')
plt.legend()
plt.grid()
plt.show()