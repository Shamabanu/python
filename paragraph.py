n=(raw_input())
m=len(n)
c=1
for i in range(0,m):
    if(n[i]=="."):
        c=c+1
    else:
        c=c
print(c)
