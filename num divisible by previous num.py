num = int(input())
arr = list(map(int,input().split()))
s = []
for i in range(1,num):
    if(arr[i]%arr[i-1] == 0):
        s.append(arr[i])
print(*s)
