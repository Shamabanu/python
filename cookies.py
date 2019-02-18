a,b=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
m1=0
m2=0
for x in range(0,len(a1)):
    m1=m1+a1[x]
    m2=m2+a2[x]
print(m2//m1)
