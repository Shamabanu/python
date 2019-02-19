s1=str(input())
n=[]
for j in s1:
    if(j not in n):
        n.append(j)
n.reverse()
l1="".join(map(str,n))
print(l1)
