num=input().split()
m=[]
for j in num:
    m.append(j[::-1])
for i in range(0,len(m)):
    if(i==len(m)-1):
        print(m[i],end=(""))
    else:
        print(m[i],end=(" "))
