s=str(input())
o=list(s)
for x in range (0,len(s)):
    if(x%2==0):
        o[x],o[x+1]=o[x+1],o[x]
print(''.join(o))
