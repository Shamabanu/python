num=input()
m=[]
s=0
for i in range(0,len(num)-1):
    k=int(num[i])+int(num[i+1])
    if k%2!=0:
        s=s+1
    else:
        m.append(s)
        s=0
    m.append(s)
n=max(m)
if n==0:
    print(0)
else:
    print(n+1)
