Num=int(input())
l=list(map(int,input().split()))
p=l[0]
k=[]
k.append(p)
for i in range(1,len(l)):
    p=p+l[i] 
    k.append(p)
k.append(l[len(l)-1])
a=l[len(l)-1]
for j in range(len(l)-2,-1,-1):
    a=a+l[j] 
    k.append(a)
print(max(k))
