m,n=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(0,m):
    if(arr[i]==n):
        print("yes")
        break
else:
    print("no")
