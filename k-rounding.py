n,k=map(int,input().split())
temp1=str(n)
temp2='0'*k
val=n
upr=10
if(k>0):
	while(1):
		if(temp1[len(temp1)-k:len(temp1)]==temp2 and val%n==0):
			break
		else:
			val=n*upr
			temp1=str(val)
			upr+=10

print(val)
