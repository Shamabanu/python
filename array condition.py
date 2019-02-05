m,n=map(int,input().split())
s=input().split()
f=0
for i in range(0,len(s)):
    c=0
    if(i==len(s)-1):
        c=int(s[0])+int(s[i])
    else:
        c=int(s[i])+int(s[i+1])
    if(c==n):
        f=f+1
if(f>0):
    print("yes")
else:
    print("no")
