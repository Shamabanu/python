n,m=input().split()
n=int(n)
m=int(m)
if(n==1 and m==1):
    print(1)
for i in range(2,100):
    if(n%i==0 and m%i==0):
        print(i)

