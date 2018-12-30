k=input().split()
k=list(map(int,k))
s=input().split()
s=list(map(int,s))
c=[]
for i in range(k[1]):
  d=input().split()
  c.append(list(map(int,d)))
for i in range(k[1]):
  print(min(s[(c[i][0]-1):c[i][1]]))
