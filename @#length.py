def player_53():
	m=input()
	m+='\0'
	c=0
	x=0
	while(True):
		if m[x]=='\0':
			break
		c+=1
		x+=1
	print(c)
player_53()
