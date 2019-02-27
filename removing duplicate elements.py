num=int(input())
arr=list(map(int,input().split()))
s=[]
for i in arr:
    if(i not in s):
        s.append(i)
print(*s)
