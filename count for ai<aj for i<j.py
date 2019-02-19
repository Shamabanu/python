num=int(input())
s=input().split()
k=0
for x in range(num-1,-1,-1):
    for y in range(0,x+1):
        if(s[x]>s[y]):
            k=k+1
print(k)
