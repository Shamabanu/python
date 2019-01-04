arr=str(input())
k=[]
for x in arr:
    if(x=='z' or 'Z'):
        x=chr(ord(x)-23)
        k.append(x)
    else:
        x=chr(ord(x)+3)
        k.append(x)
m=''.join(k)
print(m)
