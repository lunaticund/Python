import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,4*np.pi,300)

y=np.sin(np.cos(x)*x)

plt.plot(x,y)

plt.show()