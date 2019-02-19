num= int(input(""))
arr = list(map(int,input().split()))
u,v = map(int,input().split())
x =[index for index, value in enumerate(arr) if value == u]
y = [index for index, value in enumerate(arr) if value == v]
dist = num
for i in range(len(x)):
    for j in range(len(y)):
        if(x[i]>y[j]):
            d = x[i]-y[j]
        else:
            d = y[j]-x[i]
        if(d<dist):
            dist = d
print(dist)

