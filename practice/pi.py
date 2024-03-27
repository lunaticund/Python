import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 创建一个新的figure
fig = plt.figure()

# 添加一个3D子图
ax = fig.add_subplot(111, projection='3d')

# 定义x, y数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
print(x)
print(y)
# 定义z数据（例如，一个简单的函数 z = x^2 + y^2）
z = x**2 + y**2

# 使用plot_surface绘制三维网格图
surface = ax.plot_surface(x, y, z, cmap='viridis')

# 添加颜色条
fig.colorbar(surface)

# 设置坐标轴标签
ax.set_xlabel('X 轴')
ax.set_ylabel('Y 轴')
ax.set_zlabel('Z 轴')

# 显示图形
plt.show()
