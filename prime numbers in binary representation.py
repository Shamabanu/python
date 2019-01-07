m,n=input().split()
m=int(m)
n=int(n)
p=[]
d=0
for i in range(m,n+1):
    s=list(bin(i))
    del s[1]
    s=map(int,s)
    p.append(sum(s))
for i in p:
    if(i>1):
       for j in range(2,i):
           if i%j==0:
               break
       else:
            d+=1
print(d)
