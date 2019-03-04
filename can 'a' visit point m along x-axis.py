x,y=map(int,input().split())
m=0
for i in range(x):
  p,q=map(int,input().split())
  if y in range(p,q+1):
    m=1
if(m==1):
  print("yes")
else:
  print("no")
