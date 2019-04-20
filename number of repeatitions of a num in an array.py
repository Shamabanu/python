n,k=map(int,input().split())
s=0
m=[int(i) for i in input().split()]
for i in range(0,n):
    if(k==m[i]):
        s=s+1
print(s)        
