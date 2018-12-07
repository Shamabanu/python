m,n=map(str,(input()).split())
O=0
for i in range(0,len(m)):
    if((ord(m[i])-ord(m[i-1]))!=(ord(n[i])-ord(n[i-1]))):
        O=O+1
if(O>0):
    print("no")
else:
    print("yes")
