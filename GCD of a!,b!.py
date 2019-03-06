def factorial(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
num,m=map(int,(input()).split())
q=min(m,num)
k=factorial(q)
print(k)
