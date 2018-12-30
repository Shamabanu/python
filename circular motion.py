def pro_23():
    s=input()
    st=list(s)
    n,e,s,w=(0,1,2,3)
    dir=n
    x,y=0,0
    for move in st:
        if(move == 'L'):
            dir=(dir+1)%4
        elif(move == 'R'):
            dir=(4+dir-1)%4
        else:
            if(dir==n):
                y+=1
            elif(dir==e):
                x+=1
            elif(dir==w):
                x-=1
            elif(dir==s):
                y-=1
    if(x==0 and y==0):
        print("yes")
    else:
        print("no")
pro_23()

