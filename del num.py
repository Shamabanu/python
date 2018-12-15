a,b=input().split()
a=int(a)
b=int(b)
c=list(str(a))
e=b
while e>0:
    e=e-1
    del(c[e])
print(''.join(c))
