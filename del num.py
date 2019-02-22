m,n=input().split()
n=int(n)
c=len(m)
d1=[]
for i in range(0,c):
	s=m[i]
	d1.append(s)
w=c-n
t=[]
for j in range(n,c):
	s=d1[j]
	t.append(s)
print("".join(t))
