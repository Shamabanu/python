p,q = (input().split())
p = int(p)
q = int(q)
c=0
for m in range(p,q+1 ):
   if m > 1:
       for i in range(2,m):
           if (m % i) == 0:
               break
       else:
           c=c+1
print(c)  
