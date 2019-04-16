def looping(n):
  x=0
  while(x<(n+int(n/2))):
    u=2
    while(u<=n):
      if(x+1==(n+int(n/2))):
        print(u)
        return
      else:
        print(u,end=' ')
        u+=2
        x+=1
    u=1
    while(u<=n):
      if(x+1==(n+int(n/2))):
        print(u)
        return
      else:
        print(u,end=' ')
        u+=2
        x+=1    
n=int(input())
print(n+int(n/2))
looping(n)
