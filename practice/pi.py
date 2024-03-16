import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return -np.e**(-x)/(x**2)

x=np.linspace(0.5,3,300)
y=func(x)

plt.plot(x,y)
plt.grid()
plt.show()