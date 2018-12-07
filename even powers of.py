n=int(input())
m=[]
for x in range(1,n+1):
    if(n%x==0 and x%2==0):
        m.append(x)
s=" ".join(map(str,m))
print(s)
