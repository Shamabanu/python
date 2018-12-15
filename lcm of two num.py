L,R=input().split()
L=int(L)
R=int(R)
if(L>R):
    g=L
else:
    g=R
while(True):
    if((g%L==0) and (g%R==0)):
        l=g
        break
    g+=1
print(l) 
