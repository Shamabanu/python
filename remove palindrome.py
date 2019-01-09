s=input()
m=''
k=list(reversed(s))
q=''.join(k)
if(s==q):
    for n in range(0,len(s)-1):
        m=m+s[n]
    print(m)
else:
    print(s)
        
