def repeat(m,n,c):
  d=[]
  for i in range(n):
    f=0
    for j in range(1,m):
      if(c[0][i] in c[j]):
        f+=1
    if((f+1)==m and c[0][i] not in d):
      d.append(c[0][i])
  d=sorted(d)
  for i in range(len(d)):
    if(i==0):
      print(d[i],end='')
    else:
      print('',d[i],end='')    

m=input().split()
m=list(map(int,m))
n=[]
for i in range(m[0]):
  n.append(list(map(int,input().split())))
repeat(m[0],m[1],n)
