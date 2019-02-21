n1,n2=map(int,input().split())
m1,m2=map(int,input().split())
c1,c2=map(int,input().split())
if(n1==m1==c1 or n2==m2==c2 or n1+m1+c1==n2+m2+c2):
    print("yes")
else:
    print("no")
