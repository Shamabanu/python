m,n=(input().split())
m=int(m)
n=int(n)
  
if m > n: 
    small = n 
else: 
    small = m 
for i in range(1, small+1): 
    if((m % i == 0) and (n % i == 0)): 
        gcd = i 
print(gcd) 
