n,m=map(int,input().split())
arr=list(map(int,input().split()))
a=[]
c=arr[:n]
#print(c)
d=arr[n:]
#print(d)
for i in c:
    if(i in d):
        a.append(i)
a=sorted(a)        
print(" ".join([str(i) for i in a]))
