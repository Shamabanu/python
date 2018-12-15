n=input()
a=len(n)
s=list(n)
if(a%2==0):
    m=a/2 - 1
    k=int(m)
    s[k]='*'
    s[k+1]='*'
else:
    m=a/2 - 1
    k=int(m)
    s[k+1]='*'
print("".join(s))
