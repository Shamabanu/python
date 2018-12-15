m,n=input().split()
m=int(m)
n=int(n)
s=input().split()
k=input().split()
s.sort()
k.sort()
s1=''.join(s)
s2=''.join(k)
if(s2 in s1):
    print("YES")
else:
    print("NO")
