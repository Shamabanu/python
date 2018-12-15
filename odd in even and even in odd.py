num=int(input())
b=input().split()
c=len(b)
k=[]
for i in range(0,c):
	if i%2==0:
		b[i]=int(b[i])
		if b[i]%2!=0:
			k.append(b[i])
	else:
		b[i]=int(b[i])
		if b[i]%2==0:
			k.append(b[i])
s=' '.join(map(str,k))
print(s)
