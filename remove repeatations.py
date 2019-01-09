s=input()
a=[]
for x in s:
    if(x not in a):
        a.append(x)
m=''.join(a)
print(m)

