val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = str(input())
s = s.upper()
t = 0
while s:
    if len(s) == 1 or val[s[0]] >= val[s[1]]:
        t += val[s[0]]
        s = s[1:]
    else:
        t += val[s[1]] - val[s[0]]
        s = s[2:]
print (t)
