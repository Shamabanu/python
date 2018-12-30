p=input().split()
s=0
for i in p:
    if(s<len(p)):
        if(s%2==0):
            p[s]=i[::-1]
            s=s+1
        else:
            s=s+1
m=" ".join(map(str,p))
print(m)
