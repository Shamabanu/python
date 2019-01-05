n,p,q,r=input().split()
n=int(n)
p=int(p)
q=int(q)
r=int(r)
l=[]
max=-1
l=list(map(int,input().split()))
l.sort()
for i in range(n):
	for j in range(n):
            for k in range(n):
                sum=(p*l[i])+(q*l[j])+(r*l[k])
                if max<sum:
                        max=sum
print(sum)

