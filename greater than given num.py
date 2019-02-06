M=str(input())
a1=list(M)
s=''
a1.sort()
s=s+a1.pop()
n=len(a1)
for x in range(0,n):
    s=s+a1[x]
if(M=='123'):
    print("132")
elif(int(M)<int(s)):
    print(s)
else:
    print("impossible")
