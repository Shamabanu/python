m,n=map(int,input().split())
c=m*n
p=bin(c)
k=p[::-1]
for i in range(0,len(k)):
    if(k[i]=='1'):
        print(i+1)
        break
