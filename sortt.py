k=int(input())
nar=[]
for i in range(k):
    nar.extend(input().split())
nar=[int(x) for x in nar]
nar.sort()
for i in nar: print(i,end=" ")

