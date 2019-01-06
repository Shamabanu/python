n=int(input())
m=input().split()
a=[]
p=0
for i in m:
    a.append(int(i))
for i in a:
    if(a.count(i)==1):
        print(i)
