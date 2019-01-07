def permutation(b):
	if(len(b)==0):
		return []
	elif(len(b)==1):
		return [b]
	else:
		n=[]
		for i in range(len(b)):
			x=b[i]
			y=b[:i]+b[i+1:]
			for p in permutation(y):
				n.append([x]+p)
		return n
b=input()
if b.isdigit():
	data=list(b)
	q=[]
	for p in permutation(data):
		if("".join(p) not in q):
			q.append("".join(p))
	for j in q:
		print(j)
