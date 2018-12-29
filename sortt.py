n=int(input())
nar=[]
for j in range(n):
    nar.extend(input().split())
nar=[int(x) for x in nar]
nar.sort()
for j in nar: print(j,end=" ")

