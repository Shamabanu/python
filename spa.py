n=input()
b=list(n)
c=len(b)-1
for i in range(c):
    if b[i]==" ":
        b.remove(b[i])
        if i!=c-1:
            i=i+1
            c=c-1
        else:
            break
m="".join(b)
print (m)
