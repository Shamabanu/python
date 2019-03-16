s=input()
a=[]
b=[]
c=[]
for i in range(0,len(s),2):
    a.append(s[i])
k="".join(map(str,a))
for i in range(1,len(s),2):
    b.append(s[i])
m="".join(map(str,b))
for i in range(2,len(s),2):
    c.append(s[i])
n="".join(map(str,c))
for i in range(0,int(m[0])):
    print(k[0],end="")
for i in range(0,int(m[1])):
    print(k[1],end="")
for i in range(0,int(m[2])):
    print(k[2],end="")

