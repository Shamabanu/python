s,p=map(int,input().split())
e=input().split()
while(p>0):
    e.insert(0,e.pop())
    p=p-1
for x in range(0,len(e)):
    if(x!=len(e)-1):
        print(e[x],end=(" "))
    else:
        print(e[x])
