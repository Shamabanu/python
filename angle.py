a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if(a!=0 and b!=0 and c!=0):
    if(a+b+c==180):
        print("yes")
else:
    print("no")
