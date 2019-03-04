s = list(map(str,input().split()))
for x in range(len(s)):
    if(x != 0 and x != (len(s)-1)):
        s[x] = s[x][::-1]
print(" ".join(map(str,s)))
