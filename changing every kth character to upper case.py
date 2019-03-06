s,num=map(str,(input()).split())
num=int(num)
arr=[]
for i in range(0,len(s)):
    if((i+1)%num==0):
        arr.append(s[i].upper())
    else:
        arr.append(s[i])
print("".join(map(str,arr)))

