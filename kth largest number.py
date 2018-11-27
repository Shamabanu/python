N=int(input())
K=int(input())
arr=[]
for i in range(0,N):
    arr.append(int(input()))
arr.sort()
print(arr[N-K])
