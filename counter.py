n = int(input())
k = 3
a = k
while(n>0):
    if(a == 0):
        k = 2*k
        a = k
    if(n==1):
        print(a)
        break
    n -= 1
    a -= 1
