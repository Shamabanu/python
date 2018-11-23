x=int(input())
y=int(input())
if(x>y):
    g=x
else:
    g=y
while(True):
    if((g%x==0) and (g%y==0)):
        l=g
        break
    g+=1
print(l)    
