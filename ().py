s=input()
p=0
for i in range(0,len(s)):
    if(s[i]=='('):
        p=p+1
    if(s[i]==')'):
        p=p-1
if(p==0):
    print("yes")
else:
    print("no")
