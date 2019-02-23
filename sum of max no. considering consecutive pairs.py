num=int(input())
l1=list(map(int,input().split()))
m=0
for i in range(0,len(l1)-1):
    m=m+max(l1[i],l1[i+1])
print(m)
