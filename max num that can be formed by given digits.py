n=(input())
a=[]
for i in n:
    a.append(i)
a.sort()
s="".join(map(str,a))
print(s[::-1])
