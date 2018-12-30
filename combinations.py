m=int(input())
s=[]
for x in range(0,2**m):
    s.clear()
    s.append(format(x,"b"))
    k="".join(map(str,s))
    while(len(k)!=m):
        k='0'+k
    if(x!=(2**m)-1):
        print(k,end=("\n"))
    else:
        print(k)
