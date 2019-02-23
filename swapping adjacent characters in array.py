num=int(input())
arr=list(map(int,input().split()))
for x in range(0,num-1,2):#range is 0,2,4,.....num-1
    arr[x],arr[x+1]=arr[x+1],arr[x]
m=" ".join(map(str,arr))
print(m)
