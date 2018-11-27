l=(raw_input())
p=len(l)
s=1
for i in range(0,p):
    if(l[i]=="."):
        s=s+1
    else:
        s=s
print(s)
