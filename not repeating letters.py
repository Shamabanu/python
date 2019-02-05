s1=str(input())
a=[]
for j in s1:
    if(j not in a):
        a.append(j)

for i in a:
    if(s1.count(i)==1):
        print(i,end=(""))
