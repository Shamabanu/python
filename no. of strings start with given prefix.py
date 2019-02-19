n = int(input())
arr = list(map(str,input().split()))
p = input()
count = 0
for i in arr:
    if(i.startswith(p)):
        count=count+1
print(count)
