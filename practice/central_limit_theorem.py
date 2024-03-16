import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b):
    return a*np.exp(-b*x*x)

num=int(input())

dis=[]
for _ in range(num):
    list_xi=[]
    for i in range(10):
        x_i=random.uniform(-1,1)
        list_xi.append(x_i)
    dis.append(sum(list_xi)/np.sqrt(len(list_xi)))

list_yi=[]
for _ in range(600):
    list_yi.append(0)


mark=0
cnt=0
for xi in dis:
    mark=int(xi//0.01)+300
    if mark<600:
        cnt+=1
        list_yi[mark] += 100*1/num

list_x=[]


for i in range(600):
    list_x.append((i-300)*0.01)


# coef,pcov=curve_fit(func,list_x,list_yi)
# print(coef)
# x_fit=np.linspace(-3,3,num=1000)

# y_fit=func(x_fit,*coef)

plt.plot(list_x,list_yi, label='fit')
plt.legend()
plt.grid()
plt.title('Central limit theorem')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


