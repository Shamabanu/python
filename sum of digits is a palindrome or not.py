num=input()
s1=0
for x in num:
    s1=int(x)+s1
s1=str(s1)
m=s1[::-1]
if(s1==m):
    print("YES")
else:
    print("NO")
