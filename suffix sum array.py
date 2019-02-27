num=int(input())
arr=list(map(int,input().split()))
m=[]
for i in range(0,num) :
    m.append(sum(arr[i:]))
print(" ".join([str(i) for i in m]))
