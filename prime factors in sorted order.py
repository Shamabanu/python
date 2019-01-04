a=int(input())
y=[]
for j in range(2,a+1):
    if(a%j==0):
        c=0
        for x in range(1,j+1):
            if(j%x==0):
                c=c+1
        if(c==2):
            y.append(j)
for m in range(0,len(y)):
    if(m==len(y)-1):
        print(y[m])
    else:
        print(y[m],end=(' '))
