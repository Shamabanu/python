p = input()
n = len(p)
s2 = ''
m = n
x=0
while m>0:
    k=0
    c = p[x]
    while x<n and p[x] == c :
        k = k+1
        x = x+1
    if k>1 :
        s2 = s2 + str(k) + '*' + c
        m = m-k
    else :
        s2 = s2 + c
        m = m-1
print(s2)
