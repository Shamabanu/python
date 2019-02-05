Num=int(input())
m=(input().split())
n=(input()).split()
a=[]
for i in range(0,Num):
    if (n[i]in m):
        a.append(n[i])
print(" ".join(a)) 
