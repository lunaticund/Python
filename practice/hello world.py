# import numpy as np
# import matplotlib.pyplot as plt

# x=np.linspace(0,4*np.pi,300)

# y=np.sin(np.cos(x)*x)

# plt.plot(x,y)

# plt.show()

# def count(a,*b):
# 	print(len(b))

# count(1,2,3,4)
import matlab.engine

# 启动MATLAB引擎
eng = matlab.engine.start_matlab()

# 创建一些数据
x = matlab.double(range(10))
y = matlab.double([i**2 for i in range(10)])

# 调用MATLAB的plot函数
eng.plot(x, y)

# 保持MATLAB图形窗口打开
input()
