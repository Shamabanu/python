m,n=map(int,input().split())
c=m*n
k=0
p=bin(c)
for i in range(0,len(p)):
    if(p[i]=='1'):
        k=k+1
print(k)
