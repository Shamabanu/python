m,n=map(int,input().split())
c=m|n
z=bin(c)
p=z.count('1')
print(p)
