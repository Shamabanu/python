a,b=map(int,input().split())
m=''
v=2
if(a+b<=3):
    for i in range(0,a+b):
        if(i%2!=0):
            m=m+'0'
        else:
            m=m+'1'
else:    
    for i in range(0,a+b):
        if(i==v):
            m=m+'0'
            if(v==b):
                v=v+2
            else:
                v=v+3
        else:
            m=m+'1'
x=len(m)-1
if(int(m[x])==0):
    print('-1')
else:
    print(m)
