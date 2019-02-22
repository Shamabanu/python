num = int(input())
arr = list(map(int,input().split()))
s = arr[0]
for x in range(1,num):
    s = s|arr[x]
print(s)
