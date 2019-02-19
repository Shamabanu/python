n,m=map(int,input().split())
k=list(map(int,input().split()))
j=0
c=0
while j<len(k):
  if k[j]+m<=5:
    c=c+1
  j=j+1
print(c//3)
