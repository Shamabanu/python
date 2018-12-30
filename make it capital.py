num=input()
u=0
k=[]
for x in range(0,len(num)):
    if(num[x].isspace()):
        u=u
        k.append(num[x])
    elif(u%2!=0):
        k.append(num[x])
        u=u+1
    else:
        k.append(num[x].upper())
        u=u+1
q="".join(map(str,k))
print(q)
