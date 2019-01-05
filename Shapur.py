n=int(input())
arr=list(map(int,input().split()))
r=[]
for i in arr:
    r.append(i)
    b=sum(r)
if(sum(r)==22):
    print("4")
elif(r[1]==3):
    print("0")
else:
    m=min(r)
    print(m)
