num=int(input())
mark=1
print(f'1',end="")
while True:
    mark=1
    for x in range(2,int(num/2)+1):
        if num%x==0:
            mark=0
            print(f'*{x}',end="")
            num=num/x
            break
    if(mark==1):
        break
print(f'*{int(num)}')