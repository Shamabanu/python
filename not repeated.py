def count(str):
	(maxi,k)=(-1,0)
	r=[]
	for i in range(len(str)):
		if str[i] in r:
			continue
		r.append(str[i])
		for j in range(len(str)):
			if str[i]==str[j] :
                            k=k+1
		if k==1:
			print(str[i])
		k=0
def main():
	try:
		n=int(input())
		arr=[]
		arr=list(map(int,input().split()))
		count(arr)
	except:
		print('invalid')
main()
