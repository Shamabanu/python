m=int(input())
arr=list(map(int,input().split()))
s=0
arr.sort()
for i in range(0,m-1):
    s=s+arr[i] 
    if(s>arr[i+1]):
        break
print(i+2)
        
