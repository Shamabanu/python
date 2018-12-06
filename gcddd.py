x,y=(input().split())
x=int(x)
y=int(y)
  
if x > y: 
    small = y 
else: 
    small = x 
for i in range(1, small+1): 
    if((x % i == 0) and (y % i == 0)): 
        gcd = i 
print(gcd) 
