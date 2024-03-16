# n=int(input())
# prime=[2]
# for x in range(3,n+1):
#     for i in prime:
#         if x%i==0:
#             break
#     else:
#          prime.append(x)
            
# print(*prime,sep='\n')


num=int(input())
prime=list(range(2,num+1))

for x in prime:
    for xi in prime:
        if xi==x:
            continue
        if xi%x==0:
            prime.remove(xi)

print(prime)
        