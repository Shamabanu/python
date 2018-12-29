n=int(input())
if(n==3):
    print(3)
elif (n<=1000000000000000000000000000000000000000000000):
    a=1
    for i in range(1,n):
        a=a*i
    print(a)
else:
    print("invalid")
