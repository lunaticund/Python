# n=int(input())
# for x in range(n+1):
#     num=str(x)
#     if len(num)==1:
#         pass
#     else:
#         for i in range(len(num)//2):
#             if num[i]!=num[len(num)-1-i]:
#                 break
#         else:
#             print(num,end=",")


# n=int(input())
# for x in range(1,n+1):
#     x=str(x)
#     if '7'in x or int(x)%7==0:
#         print(int(x),end=" ")


# import math
# n=int(input())
# e=1
# jie=1
# for x in range(1,n+1):
#     jie = jie*x
#     e += 1/jie
# print(f'{e:.5f}')
# print(math.e)

# import numpy as np
# stand=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
# num=list(input())
# num=list(map(int,num))
# print(np.average(num,weights=stand)%11,len(stand),len(num))
# match int(np.average(num,weights=stand)%11):
#     case 0:
#         t=1
#     case 1:
#         t=0
#     case 2:
#         t='x'
#     case 3:
#         t=9
#     case 4:
#         t=8
#     case 5:
#         t=7
#     case 6:
#         t=6
#     case 7:
#         t=5
#     case 8:
#         t=4
#     case 9:
#         t=3
#     case _:
#         t=2
# print(f"末位数字：{t}")

# n='312312'
# ls=list(n)
# l1=list(map(int,ls))
# print(l1,sum(map(int,ls)))
# line = input().split()
# while line:
# 		print(line.pop(0))


# N=int(input())
# line=list(range(1,N+1))
# i=0
# while True:
#     i+=2
#     i%=len(line)
#     del line[i]
#     if len(line)==1:
#         break
# print(*line)



# mark=0
# cnt=1
# while True:
#     if len(line)==1:
#         break
#     cnt+=1
#     mark+=1
#     if mark==len(line):
#         mark=0
#     if cnt==3:
#         line.pop(mark)
#         cnt=1
#     if mark==len(line):
#         mark=0
# print(*line)

# import numpy as np

# data=[2.567,2.565,2.569,2.570,2.571,2.568]

# d_mean=np.mean(data)
# d_std=np.std(data,ddof=1)
# d_wo=d_std/np.sqrt(len(data))

# print(d_mean,d_wo)




# import matplotlib
# matplotlib.use('TkAgg')  # 或者 'Qt5Agg', 'GTK3Agg', 'MacOSX' 等


# import matplotlib.pyplot as plt
# import numpy as np

# # 定义 x 变量的范围 (-3，3) 数量 50
# x = np.linspace(-3, 3, 500)
# y = x

# # 创建一个图像窗口
# plt.figure(num=1, figsize=(8, 5))

# # 绘制 y=x^2 的图像，设置 color 为 red，线宽度是 1，线的样式是 --
# plt.plot(x, y, color='red', linewidth=1.0, linestyle='-')

# # 设置 x，y 轴的范围以及 label 标注
# plt.xlim(-1, 2)
# plt.ylim(-2, 3)
# plt.xlabel('x')
# plt.ylabel('y')

# # 设置坐标轴刻度线
# new_ticks = np.linspace(-1, 2, 5)
# plt.xticks(new_ticks)
# plt.yticks([-2, -1.5,-1,-0.5,0.5, 1, 1.5, 2])

# # 设置坐标轴
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))

# # 设置标签
# ax.set_title('y = x^2', fontsize=14, color='r')

# # 显示图像
# plt.show()





# import numpy as np

# # 构造数据
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 5, 6, 9])

# # 拟合一次多项式（线性拟合）
# coef,cov = np.polyfit(x, y, 1,cov=True)

# # 输出结果
# print(coef,np.sqrt(np.diag(cov)))


# # 计算相关系数
# correlation_matrix = np.corrcoef(x, y)
# correlation_xy = correlation_matrix[0,1]
# print(correlation_xy)


# import numpy as np
# import matplotlib.pyplot as plt

# # 构造数据
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 5, 6, 9])

# # 拟合一次多项式（线性拟合）
# coef = np.polyfit(x, y, 1)

# # 计算拟合线的y值
# y_fit = coef[0] * x + coef[1]

# plt.grid(True, which='both', axis='both', linestyle='-')

# # 绘制原始数据点
# plt.scatter(x, y, color='blue', label='Original data')

# # 绘制拟合线
# plt.plot(x, y_fit, color='red', label='Fitted line')

# # 添加图例
# plt.legend()

# # 显示图像
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

# # 定义你想要拟合的函数形式，例如指数函数
# def func(x, a, b, c):
#     return a * np.exp(b * x) + c

# # 示例散点数据
# x_data = np.array([1, 2, 3, 4, 5, 6])
# y_data = np.array([1.2, 1.9, 3.2, 10, 25, 60])

# # 使用curve_fit函数进行非线性拟合
# popt, pcov = curve_fit(func, x_data, y_data)
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False
# # 生成拟合曲线的x值和y值
# x_fit = np.linspace(min(x_data), max(x_data), 100)
# y_fit = func(x_fit, *popt)

# # 绘制原始散点和拟合曲线
# plt.scatter(x_data, y_data,c="blue",marker="x", label='原始数据')
# plt.plot(x_fit, y_fit, 'r',linestyle="-", label='拟合曲线')
# plt.legend()
# plt.grid()
# plt.xlabel('电压(V)')
# plt.ylabel('电流(A)')
# plt.title('非线性拟合')
# plt.show()


