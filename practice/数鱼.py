N=x=0
while True:
    N=N+1
    x=N
    for _ in range(4):
        x=4*(x-1)/5
    if (x-1)%5==0:break
print(N)