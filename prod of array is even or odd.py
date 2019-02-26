n=int(input())
a=list(map(int,input().split()))
s=1
for i in range(0,n):
    s=s*a[i]
if(s%2==0):
    print("even")
else:
    print("odd")
