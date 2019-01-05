import sys, string, math
from itertools import permutations,combinations

n,k = input().split()
n,k = int(n),int(k)
LW = [ int(x) for x in input().split()]
LV = [ int(x) for x in input().split()]
d1 = {}
for i in range(0,n) :
    if LW[i] not in d1 :
        d1[LW[i]] = [LV[i]]
    else :
        d1[LW[i]].append(LV[i])

L3 = []
for i in range(1,n+1) :
    L2 = list(combinations(LW,i))
    for x in L2 :
        if sum(x) <= k :
            L3.append(x)
max1 = 0
for x in L3 :
    sum1 = 0
    d2 = {}
    for i in x :
        if i not in d2 :
            d2[i]= d1[i][:]
    for i in x :
        if len(d2[i]) == 1 :
            sum1 += d2[i][0]
        else :
            a = max(d2[i])
            sum1 += a
            d2[i].remove(a)
    if sum1 > max1 :
        max1 = sum1
print(max1)

