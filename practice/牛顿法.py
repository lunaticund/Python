import math

n=float(input())#给定需要的精度
x=1
#Newton法进行迭代
while abs(x*x*x+math.log(x)+1)>n):
			x = x-(x*x*x+math.log(x)+1)/(3*x*x+1/x)
print(x)