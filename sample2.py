num=int(input())
l1=[]

k=list(map(int,input().split()))
p=len(k)
if(p<=3):
    print(1)
else:
    while(p>3):
        for x in range(0,p):
            if(x%2!=0):
                k[x]=0
        for y in k:
            if(y>0):
                l1.append(y)
        k.clear()
        k=l1.copy()
        p=len(k)
    print(p)
