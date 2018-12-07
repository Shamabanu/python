z=str(input())
o=list(z)
for x in range (0,len(z)):
    if(x%2==0):
        o[x],o[x+1]=o[x+1],o[x]
print(''.join(o))
