num=int(input())
arr=list(map(int,input().split()))
m=[]
for i in range(len(arr)+1): 
    for j in range(i+1,len(arr)+1): 
        m.append(arr[i:j])
print(len(m)) 
