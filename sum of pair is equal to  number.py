a,b=map(int,input().split())
d=0
l=list(map(int,input().split()))
for i in range(0,a):
    for j in range(i,a):
        if(b==l[i]+l[j]):
            d=d+1
if(d>1):
    print("YES")
else:
    print("NO")
