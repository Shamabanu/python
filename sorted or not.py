k=int(input())
s=input().split()
m=1
for x in range(0,len(s)-1):
    if(s[x]<=s[x+1]):
        m=m+1
if(m==len(s)):
    print("yes")
else:
    print("no")
