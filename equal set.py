a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=b*4+c*4
if(a==2 and b==1 and c==1):
    print("YES")
elif(a==d):
    print("YES")
else:
    print("NO")
