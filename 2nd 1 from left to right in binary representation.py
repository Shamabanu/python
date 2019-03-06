m,n=map(int,input().split())
c=m*n
p=bin(c)
for i in range(3,len(p)):
    if(p[i]=='1'):
        print(i-1)
        break
