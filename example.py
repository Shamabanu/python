def main():
	n,m=input().split()
	n=int(n)
	m=int(m)
	r=[]
	for x in range(n):
            l=list(map(int,input().split()))
            r.append(l)
            l=[]
	for i in r:
		i.sort()
	(s,w)=([],[])
	for i in range(m):
		for j in range(n):
			s.append(r[j][i])
		w.append(s)
		s=[]
	r=[]
	for i in w:
		i.sort()
	for i in range(n):
		for j in range(m):
			r.append(w[j][i])
		print(r)
		r=[]
try:
	main()
except:
	print('invalid')

