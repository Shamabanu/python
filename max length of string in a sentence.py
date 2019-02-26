s = list(map(str,input().split()))
max = len(s[0])
r = s[0]
for i in s:
    if(len(i)> max):
        max = len(i)
        r = i
print(r)
