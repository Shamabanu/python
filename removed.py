n=int(input())
m=input()
p="".join(reversed(m))
for i in "aeiouAEIOU":
    p=p.replace(i,"")
print(p)
