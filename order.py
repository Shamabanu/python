m=int(input())
n=0
a=list(map(int,input().split()))
for i in range(0,m-1):
    if(a[i]>a[i+1]):
        n=n+1
        print(i)

    
