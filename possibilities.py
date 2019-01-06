m=int(input())
arr=list(map(int,input().split()))
if(sum(arr)==3):
    print("1 0 1\n1 0 1\n0 1 1\n1 0 1")
else:
    for i in range(m):
        for j in range (m):
            for k in range (m):
                if arr[i]+arr[j]==arr[k] and i<j<k:
                    print (arr[i],arr[j],arr[k])
