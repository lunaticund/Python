import matlab.engine

   # 启动MATLAB引擎
eng = matlab.engine.start_matlab()

   # 定义x, y, z用于绘制图形
x = [[i for i in range(10)] for j in range(10)]
y = [[j for i in range(10)] for j in range(10)]
z = [[i*j for i in range(10)] for j in range(10)]

   # 转换为MATLAB数组
mx = matlab.double(x)
my = matlab.double(y)
mz = matlab.double(z)

   # 绘制三维曲面图
eng.surf(mx, my, mz, nargout=0)
input()
   # 显示图形
eng.show(nargout=0)


