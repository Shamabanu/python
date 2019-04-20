n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
m=[]
for i in range(len(a1)-1,-1,-1):
    m.append(a1[i])
if(a2==m):
    print("yes")
else:
    print("no")
