a=int(input())
b=input().split()
d=len(b)
for i in range(0,d):
	z=b.count(b[i])
	if (z<2):
		print(b[i])
