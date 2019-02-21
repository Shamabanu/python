num=int(input())
arr=(input().split())
arr.sort()
l1=[]
s=[]
for x in arr:
    l1.append(len(x))
l1.sort()
for x in l1:
    for y in arr:
        if(len(y)==x):
            if y not in s:
                s.append(y)
for i in s:
    print(i,end=" ")
