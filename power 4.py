n=int(input())
tot=0
for i in range(0,len(str(n))):
    dig=n%10
    m=dig**4
    tot=tot+m
    n=n//10
print(tot)
