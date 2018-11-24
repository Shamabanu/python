N=int(input())
K=int(input())
a=[]
for i in range(0,N):
    a.append(int(input()))
a.sort()
print(a[N-K])
