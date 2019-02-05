a,b=map(int,input().split())
l=input().split()
l2=[]
s=[]
for i in l:
    l2.append(int(i))
for j in l2:
    if(j<b):
        s.append(j)
s.sort()
m=" ".join(map(str,s))
print(m)
