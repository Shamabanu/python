def sumpair(S,K,c):
  for i in range(S):
    for j in range(i+1,S):
      if((c[i]+c[j])==K):
        return('yes')
  return('no')
a=(input()).split()
a=list(map(int,a))
b=(input()).split()
b=list(map(int,b))
print(sumpair(a[0],a[1],b))
