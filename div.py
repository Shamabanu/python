def fun(s,n):
    print(s[n:]+s[:n])
s,n=map(str,input().split())
n=int(n)
k=len(s)-n
fun(s,k)
