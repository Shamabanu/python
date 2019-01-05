m=(input())
arr=[]
s=0
for x in m:
    if not x in arr:
        s+=1
        arr.append(x)
    else:
        break
print(s)
