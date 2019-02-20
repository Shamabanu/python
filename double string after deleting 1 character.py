s1=input()
m=len(s1)
d=int(m/2)
p=s1[0:d]
q=s1[d+1:m]
if p==q:
    print("YES")
else:
    print("NO")
