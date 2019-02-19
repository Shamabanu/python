num=input()
c=0
l1=2
if(len(num)>1):
    for x in range(0,len(num)):
        if(l1<=len(num)):
            c=c+int(num[x])**l1
            l1=l1+1
        else:
            c=c+int(num[x])**1
else:
    c=int(num[0])**2
print(c)
