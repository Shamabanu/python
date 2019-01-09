n=int(input())
b=[]
l=list(map(int,input().split()))
p=1
for i in range (0,n):
    b.append(l[i])
for i in range (0,n):
    for j in range (0,n):
        if(j!=i):
            p=p*b[j]
    print(p,end=' ')
    p=1
