import sys, string, math

m = input()
if m == m[::-1] :
    print('yes')
    sys.exit()
n = 0
for i in m[::-1] :
    if i == '0' :
        n += 1
    else :
        break
s1 = '0'*n + m
if s1 == s1[::-1] :
    print('yes')
else :
    print('no')


