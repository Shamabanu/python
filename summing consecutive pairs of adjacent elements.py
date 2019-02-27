num=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(0,num-1):
    s=s+arr[i]+arr[i+1]
print(s)
