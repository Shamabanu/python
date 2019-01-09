k=int(input())
m=[[int(i) for i in input().split()]for j in range(k)]
p=sum(m[i][i] for i in range(k))
p1=sum(m[i][k-i-1] for i in range(k))
if k%2!=0:
    print(p+p1-m[k//2][k//2])
else:

    print(p+p1)
