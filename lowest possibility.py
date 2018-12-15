a,b=input().split()
a=list(a)
b=list(b)
d=len(a)
e=len(b)
i=0
j=0
c=[]
while d>0:
    if a[i]==b[j]:
        c.append(a[i])
    j=j+1
    i=i+1
    d=d-1
print(e-len(c))
