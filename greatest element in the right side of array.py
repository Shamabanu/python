num = int(input(""))
arr = list(map(int,input().split()))
k =[]
for x in range(num-1):
    j = max(arr[x+1:])
    k.append(str(j))
k.append(str(0))
print(" ".join(map(str,k)))
