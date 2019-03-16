n=input()
m=""
for i in n:
    if(i==" " or n.count(i)==1):
        m=m+i
    else:
        m=m+i.upper()
print(m)
