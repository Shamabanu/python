N,K=(input()).split()
N=int(N)
K=int(K)
b=[]
a=list(map(int,input().split()))
for i in range(0,N):
    if(a[i]%2!=0):
        b.append(a[i])
c=list(''.join(map(str,b)))
print(c[K-1])
