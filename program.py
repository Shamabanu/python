k=list(map(int,input().split()))
s=list(map(int,input().split()))
q=[]
for i in range(k[1]):
  c=list(map(int,input().split()))
  m=s[(c[0]-1)]^s[(c[0])]
  for j in range(c[0]+1,c[1]):
    m=m^s[j]
  q.append(m)
for i in range(len(q)):
  print(q[i])
