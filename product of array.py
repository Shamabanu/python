n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
m=1
for x in range(0,n):
    m=m*a[x]
q=abs(m)    
print(q)    
