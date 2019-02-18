import sys
n,k=map(int,input().split())
nd=list(map(int,input().split()))
al=list(map(int,input().split()))
ck=0
f=0
if n==1:
  print((al[0]+k)//nd[0])
  sys.exit(0)
while f!=1:
  c=0
  for i in range(n):
    if al[i]>=nd[i]:
      al[i]=al[i]-nd[i]
      c+=1
    else:
      if k>=nd[i]-al[i]:
        k-=nd[i]-al[i]
        al[i]=0
        c+=1
      else:
        f=1
        break
  if c==n:
    ck+=1
print(ck)
