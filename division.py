divident,divisor=list(map(int,input().split()))
x=0
while(divident>=divisor):
    divident-=divisor
    x+=1
print(x)

