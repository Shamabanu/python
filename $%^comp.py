def player_55():
	s=input()
	l=s.split(' ')
	s1,s2=l[0],l[1]
	x=0
	a=''
	b='\0'
	while(x<len(s1)):
		if ord(s1[x]) in range(65,91):
			q=ord(s1[x])+32
			a=chr(q)
		if ord(s2[x]) in range(65,91):
			q=ord(s2[x])+32
			b=chr(q)
		if s1[x]==s2[x] or a==s2[x] or b==s1[x]:
			x+=1
		else :
			print('No')
	print("yes")
player_55()
