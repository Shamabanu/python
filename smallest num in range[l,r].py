num,p,q=map(int,(input()).split())
arr=list(map(int,(input()).split()))
m=[]
for i in range(p-1,q):
    m.append(arr[i])
print(min(m))
