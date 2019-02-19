num=int(input())
l1=input().split()
sum=[]
x,y=map(int,input().split())
for j in l1:
    sum.append(int(j))
p=sum.index(x)
q=sum.index(y)
if(p>q):
    print(p-q)
else:
    print(q-p)
