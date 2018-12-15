num=int(input())
ar=input().split()
a=" ".join(map(str,ar))
m=[]
for x in a:
    if(x not in m):
        if(a.count(x)>1):
            m.append(x)
if(len(m)>1):
    n=" ".join(m) 
    h=n[0:1]
    print(h)
else:
    print("unique")
