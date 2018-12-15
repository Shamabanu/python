n=int(input())
k=input().split()
d=len(k)
for i in range(0,d):
    z=k.count(k[i])
    if(z<2):
        print(k[i])
