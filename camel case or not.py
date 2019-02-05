l1=input()
s=-1
m=0
if(l1[0]>="A" and l1[0]<="Z"):
    s=s+1
for x in range(0,len(l1)):
    if(l1[x]==" "):
        m=m+1
        if(l1[x+1]<="Z" and l1[x+1]>="A"):
            s=s+1 
if(m==s):
    print("yes")
else:
    print("no")
