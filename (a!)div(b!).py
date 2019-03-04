a,b=map(int,input().split())
def fact(n):
    fac=1
    for x in range(1,n+1):
        fac=fac*x
    return fac
c=fact(a)//fact(b)
print(c)
