import random

N=int(input())
cnt=0
for _ in range(N):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x*x+y*y<=1:
        cnt += 1
print(4*cnt/N)
 