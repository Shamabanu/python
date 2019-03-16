m,n = map(int,input().split())
c=0
m = m^n
p=bin(m)
for i in range(2,len(str(p))):
    if(p[i]=='1'):
        c=c+1
print(c)
