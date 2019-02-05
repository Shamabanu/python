n,k=(input().split())
n=int(n)
k=int(k)
m=[]
arr=(input()).split()
for i in arr:
    if(arr.count(i)==k):
        m.append(i)
        while i in arr:
            arr.remove(i)
print("".join(m))
