n,k = input().split()
n = int(n)
k = int(k)
l = []
(s1,s2) = ([],[])
l = list(map(int,input().split()))
if(n%2!=0):
    s1=l[:n-1]
    s2=l[n-1:n]
else:
    s1=l[:n//2]
    s2=l[n//2:n]
print(max(min(s1),min(s2)))

