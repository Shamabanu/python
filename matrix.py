def checker(a,b,i,j):
  for k in range(min((a[0]-i),(a[1]-j))):
    for l in range(i,k+i+1):
      for m in range(j,k+j+1):
        if(b[l][m]==0):
          return(k)
  return(k+1)

a=list(map(int,input().split()))
b=[]
sign=0
for i in range(a[0]):
  b.append(list(map(int,input().split())))
for i in range(a[0]):
  for j in range(a[1]):
    c=b[i][j]
    if(c==1):
      z=checker(a,b,i,j)
      if(sign<z):
        sign=z
for i in range(sign):
  for j in range(sign):
    if((sign-1)==j):
      print(1)
    else:
      print(1,end=' ')
