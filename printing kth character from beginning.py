s,num=map(str,input().split())
num=int(num)
arr=[]
for i in range(num-1,len(s),num):
    arr.append(s[i])
print(*arr)

