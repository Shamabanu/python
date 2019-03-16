m,n = map(int,input().split())
c=0
m = m^n
p=bin(m)
print(p.count('1'))
