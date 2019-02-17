n=int(input())
arr=list(map(int,input().split()))
n=len(arr)
o=[]
for i in range(0,n):
  sum=arr[i]
  j=i+1
  c=1
  if sum<0:
    flag=0
    sign='n'
  else:
    flag=1
    sign='p'
  while j<n:
    if flag==0 and sign=='n' and arr[j]>0:
      j+=1
      c+=1
      flag=1
      sign='p'
    elif flag==1 and sign=='p' and arr[j]<0:
      j+=1
      c+=1
      flag=0
      sign='n'
    else:
      break
  o.append(c)
print(*o)
