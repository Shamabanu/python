k,m=map(int,input().split())
import sys
edges=[]
for j in range(m):
  edges.append(list(map(int,input().split())))

maxi=0
for i in range(m):
  if edges[i][0]==1:
    q=1
    q+=edges[i][1]
    start=edges[i][1]
    j=i+1
    while j<m:
      if edges[j][0]==start:
        q+=edges[j][1]
        start=edges[j][1]
      j+=1
  if q>maxi:
    maxi=q
print(maxi)
