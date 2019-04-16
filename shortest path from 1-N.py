a,b=map(int,(input()).split())
ki=[]
for i in range(b):
  ki.append(list(map(int,(input()).split())))
pie=10000000
f=0
for i in range(b):
  if ki[i][0]==1:
    s=ki[i][1]
    c=ki[i][2]
    for j in range(i+1,b):
      if ki[j][0]==s:
        s=ki[j][1]
        c+=ki[j][2]
    if c<pie and s==a:
      pie=c
      f+=1
if f==0:
  print(-1)
else:
  print(pie)
