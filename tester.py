#Tester program
N=int(input())
arr=input().split()
arr=list(map(int,arr))
tester=[]
for i in range(N):
  tester.append(1)
loudo=sorted(arr)
sh=[]
candy=1
for i in loudo:
  if i not in sh:
    sh.append(i)
listy=arr
if(N>1):
  for value in sh:
    position=[]
    n=0
    for i in range(len(listy)):
      if(value==listy[i]):
        n+=1
    tera=listy
    for i in range(len(tera)):
      if(tera[i]==value):
        position.append(i)
    for i in position:
      if(i==0):
        if(arr[i]>arr[i+1]):
          tester[i]=tester[i+1]+1
        elif(arr[i]==arr[i+1]):
          tester[i]=tester[i+1]
      elif(i==N-1):
        if(arr[i]>arr[i-1]):
          tester[i]=tester[i-1]+1
        elif(arr[i]==arr[i-1]):
          tester[i]=tester[i-1]
      else:
        if(arr[i]>arr[i+1] and arr[i]>arr[i-1]):
          if(arr[i+1]>arr[i-1]):
            tester[i]=tester[i+1]+1
          elif(arr[i+1]<arr[i-1]):
            tester[i]=tester[i-1]+1
        elif(arr[i]>arr[i+1] and arr[i]<arr[i-1]):
          tester[i]=tester[i+1]+1
        elif(arr[i]<arr[i+1] and arr[i]>arr[i-1]):
          tester[i]=tester[i-1]+1
        elif(arr[i]>arr[i+1] and arr[i]==arr[i-1]):
          tester[i]=tester[i+1]+1 
          if(tester[i]<tester[i-1]):
            tester[i]=tester[i-1]
        elif(arr[i]>arr[i-1] and arr[i]==arr[i+1]):
          tester[i]=tester[i-1]+1 
          if(tester[i]<tester[i+1]):
            tester[i]=tester[i+1]
        elif(arr[i]==arr[i+1] and arr[i]==arr[i-1]):
          tester[i]=tester[i-1]
          if(tester[i+1]>tester[i-1]):
            tester[i]=tester[i+1]
          else:
            tester[i]=tester[i-1]
  for i in range(N-1,0,-1):
    if(i!=N-1 and i!=0):
      if(arr[i]==arr[i+1]):
        tester[i]=tester[i+1]
print(sum(tester))
