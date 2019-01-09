n=int(input())
b=[]
l=list(map(int,input().split()))
prod=1
for i in range (0,n):
    b.append(l[i])
for i in range (0,n):
    for j in range (0,n):
        if(j!=i):
            prod=prod*b[j]
    print(prod,end=' ')
    prod=1
