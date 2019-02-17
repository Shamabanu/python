def found(t,k):
  avail=sorted(k.keys())
  for i in range(len(avail)):
    if t in avail:
      t+=1
    else:
      break
  return t
n=int(input())
a=list(map(int,input().split()))
k={}
c=0
for i in range(n):
  if a[i] not in k.keys():
    k[a[i]]=1
  else:
    k[a[i]]+=1
t=1
t=found(t,k)
ins=[]
for i in range(n):
  if k[a[i]]==1:
    ins.append(a[i])
for i in range(n):
  if k[a[i]]==1:
    ins.append(a[i])
  elif a[i] in ins:
    k[a[i]]-=1
    a[i]=t
    ins.append(t)
    k[t]=1
    t=found(t+1,k)
    c+=1
  elif a[i]>t:
    k[a[i]]-=1
    a[i]=t
    ins.append(t)
    k[t]=1
    t=found(t+1,k)
    c+=1
  else:
    ins.append(a[i])
print(c)
print(*a)
