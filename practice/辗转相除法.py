a,b=map(int,input().split())
while a%b!=0:
    a=a%b
    a,b=b,a
print(b)
