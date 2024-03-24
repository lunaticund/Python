import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#定义逆变换函数
def transfer(u):
    if u<0:
        return np.sqrt(u+1)-1
    else:
        return 1-np.sqrt(1-u)
#数据采样函数
def data():
    s=0
    for _ in range(100):
        s += transfer(random.uniform(-1,1))
    return s/10
#定义Gauss拟合函数
def gaussian(x,a,b):
    return a*np.e**(-b*(x**2))
#进行若干次采样
dic={}
for i in range(-20,20,1):
    dic[i]=0
for _ in range(10000):
    x=data()
    if x>-2.0 and x<2.0:
        dic[(x*10)//1] += 0.00001*10
        
x=list(dic.keys())
y=list(dic.values())
x=list(map(lambda x:0.1*x,x))
#拟合Gaussian函数
coef,cov=curve_fit(gaussian,x,y)
x_fit=np.linspace(-2,2,300)
y_fit=gaussian(x_fit,*coef)
#绘制图像
plt.rc('font',family='Times New Roman',size=12)
plt.plot(x_fit,y_fit,c='b',label='Fit Line')
plt.scatter(x,y,marker='x',c='r',label='Oringinal Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Centeral Limit Theorem')
plt.legend()
plt.grid()
plt.show()