num=int(input())
k=[]
for x in range(2,num):
    for y in range(2,x):
        if(x%y==0):
            break
    else:
        k.append(x)
for i in range(0,len(k)):
    if(i==len(k)-1):
        print(k[i],end=(""))
    else:
        print(k[i],end=(" "))
