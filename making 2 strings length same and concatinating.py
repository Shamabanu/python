s,m = map(str,input().split())
if(len(s)>len(m)):
    print(s[:len(m)]+m)
elif(len(m)>len(s)):
    print(s+m[:len(s)])
else:
    print(s+m)
