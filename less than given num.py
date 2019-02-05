n=int(input())
arr=(input().split())
m=[]
for i in range(0,n):
    if(int(arr[i])<n):
        m.append(arr[i])
m=sorted(m)
print(" ".join(m))
