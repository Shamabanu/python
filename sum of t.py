a=int(input())
c=0
while(a>0):
    a1=int(a%10)
    c=(a1*a1)+c
    a=int(a/10)
print(c)
