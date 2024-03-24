import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#定义采样函数
element=(-1,1)
def data():
    s=0
    for _ in range(100):
        s += random.choice(element)
    return s/np.sqrt(100)
#定义Gauss拟合函数
def gaussian(x,a,b):
    return a*np.e**(-b*(x**2))
#进行若干次采样
dic={}
for i in range(-28,30,2):
    dic[i]=0
for _ in range(10000):
    x=data()
    if x>-3.0 and x<3.0:
        dic[(x*10)//1] += 0.00001*10

x=list(dic.keys())
y=list(dic.values())
x=list(map(lambda x:0.1*x,x))
#拟合函数
coef,cov=curve_fit(gaussian,x,y)
x_fit=np.linspace(-3,3,300)
y_fit=gaussian(x_fit,*coef)
#绘制采样点和拟合图像
plt.rc('font',family='Times New Roman',size=12)
plt.plot(x_fit,y_fit,c='b',label='Fit Line')
plt.scatter(x,y,marker='x',c='r',label='Oringinal Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Centeral Limit Theorem')
plt.legend()
plt.grid()
plt.show()