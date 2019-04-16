import sys,string
def fre(s):
    mike = {}
    for c in s :
        mike[c] = mike.get(c,0) + 1
    return mike
s = input()
n = len(s)
mike = fre(s)
Mk = list(mike.keys())
for j in range(n-2,-1,-1) :
    for c in Mk :
        k = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            s2 = s[li:ri + 1]
            if(c in s2):
                k += 1
        if(k == n-j):
            c2 = c
            k2 = k
            out= j+1
print(out)
