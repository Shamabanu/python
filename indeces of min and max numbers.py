n=int(input())
a=list(map(int,input().split()))
v=max(a)
w=min(a)
for i in range(0,n):
    if(a[i]==w):
        print(i+1,end=' ')
for i in range(0,n):
    if(a[i]==v):
        print(i+1)
        
    
