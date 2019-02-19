num,m=map(int,input().split())
l1=input().split()
c=[]
for x in range(0,len(l1)):
    if(int(l1[x])!=m):
        c.append(int(l1[x]))
if(len(c)>0):
    k=" ".join(map(str,c))
    print(k)
else:
    print("empty")

