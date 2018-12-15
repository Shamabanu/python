m,n=map(int,input().split())
k=0
for x in range(1,m+1):
    if(m==(n**x)):
        k=k+1
        break
if(k==1):
    print("yes")
else:
    print("no")
