k=int(input())
l=input().split()
a=[]
s=len(l)
for su in range(0,s):
    p=int(l[su])
    if(p==su):
        a.append(su)
if(len(a)!=0):
    s=' '.join(map(str,a))
    print(s)
else:
    print("-1")
