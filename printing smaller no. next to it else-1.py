num=int(input())
l1=input().split()
m=[]
for i in l1:
    m.append(int(i))
for x in range(0,len(m)-1):
    if(m[x]>m[x+1]):
        m[x]=m[x+1]
    else:
        m[x]=-1
m[len(l1)-1]=-1
p=" ".join(map(str,m))
print(p)
