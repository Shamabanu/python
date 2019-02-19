n=int(input())
arr = list(input().split())
for i in range(0,len(arr)):
    arr[i] = arr[i].lower()
arr = sorted(arr)
print(*arr, sep="\n")

