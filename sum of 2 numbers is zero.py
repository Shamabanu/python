import sys, string, math
num = int(input())
l = list(map(int,input().split()))
l2 = []
len1 = len(l)
min = abs(l[0]+l[1])
if min == 0:
    print(l[0],l[1])
    sys.exit(1)
for i in range(0,len1-1) :
    for j in range(i+1,len1) :
        if abs(l[i]+l[j]) <= min :
            min = abs(l[i]+l[j])
            a,b = l[i],l[j]
            if min == 0 :
                print(a,b)
                sys.exit(1)
print(a,b)

