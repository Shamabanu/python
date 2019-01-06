q=int(input())
p=input().split()
a=" ".join(map(str,p))
s=[]
for i in a:
    if(i not in s):
        if(a.count(i)>1):
            s.append(i)
k="".join(s) 
print(k)
