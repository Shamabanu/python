n=int(input())
a=list(map(int,input().split()))
s=[]
b=list(map(int,input().split()))
for i in range(0,n):
    s.append(a[i]+b[i])
p=" ".join(map(str,s))
print(p)

