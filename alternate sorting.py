m=int(input())
l1=input().split()
s=[]
for x in l1:
    s.append(int(x))
s.sort()
a=[]
n=int(len(s)/2)
for x in range(0,n):
    a.append(s[len(s)-1-x])
    a.append(s[x])
if(len(s)%2!=0):
    a.append(s[n])
s=" ".join(map(str,a))
print(s)
