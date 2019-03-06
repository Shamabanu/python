l=input()
c=0
for x in range(0,len(l)):
    if(l[x]!='a' and l[x]!='b'):
        c=c+1
if(c>1):
    print("no")
else:
    print("yes")
