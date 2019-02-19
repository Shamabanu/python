num=int(input())
ways=0
arr=[]
for x in range(2,num):
  i=2
  for i in range(2,x):
    if(x%i==0):
      break
  else:
    arr.append(x)
for x in range(0,len(arr)):
    y=x
    while(y<len(arr)):
        if(arr[x]+arr[y]==num):
            ways=ways+1
        y=y+1
print(ways)
