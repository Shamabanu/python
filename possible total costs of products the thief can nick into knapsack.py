from itertools import combinations_with_replacement
a,b=map(int,input().split())
arr=list(map(int,input().split()))
k=list(combinations_with_replacement (arr,b))
out=[]
for i in k:
  if sum(i) not in out:
    out.append(sum(i))
out=sorted(out)
print(*out)
