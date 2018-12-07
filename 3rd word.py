n=str(input())
k=[]
for x in range(0,len(n),3):
    k.append(n[x])
s=''.join(map(str,k))
print(s)
