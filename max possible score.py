def fac(c1,c2):
  k=1
  for m in range(c2+1,c1+1):
    k*=m
  return k
t=int(input())
ab=[]
for m in range(t):
  ab.append(list(map(int,input().split())))
for j in ab:
  n=fac(j[0],j[1])
  c=0
  while n>1:
    x=2
    while x<n+1:
      if n%x==0:
        n=n/x
        c+=1
        break
      x+=1
  print(c)
