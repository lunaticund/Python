x=float(input())
cnt=int(input())
coef=list(map(int,input().split()))
coef.reverse()

result=coef[0]
times=1
for i in range(1,cnt):
    times*=x
    result += times*coef[i]

print(result)

n=input('按任意键返回')