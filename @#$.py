k=int(input())
c=0
for i in range(2,k):
    if(k%i==0):
        c=c+1
if(c!=0):
    print("yes")
else:
    print("no")
