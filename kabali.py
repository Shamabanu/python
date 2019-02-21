num=int(input())
s=[]
m=0
s1='kabali'
for k in range(0,num):
    s.append(str(input()))
for i in range(0,num):
    if(sorted(s[i])==sorted(s1)):
        m=m+1
print(m)

