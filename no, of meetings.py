num=int(input())
p=list(map(eval,(input()).split()))
q=list(map(eval,(input()).split()))
s=1
i=0
while (i<num-1):
  j=i+1
  while(j<num):
    if(q[i]<=p[j]):
      s=s+1
      i=j-1
      break
    j+=1
  i+=1
print(str(s))
