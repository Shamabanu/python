n,m=map(int,input().split())
k=0
while(n<2):
    n=n+1
for i in range(n,m):
    su=0
    while(i!=0):
        a=int(i%10)
        su=su+a
        i=int(i/10)
    if(su>=2):
        
        for j in range(2,su):
            
            if(su%j==0):
                break
        else:
            k=k+1
print(k)
