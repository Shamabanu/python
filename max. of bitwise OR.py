num = int(input())
arr = list(map(int,input().split()))
max = 0
for x in range(num):
    for y in range(num):
        if(arr[x]|arr[y] > max):
            max = arr[x]|arr[y]
print(max)
