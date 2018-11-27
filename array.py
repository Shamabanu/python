N=int(input())
K=int(input())
a=[]
for i in range (0, N):
    a.append(int(input()))
sum=0
for i in range(0,K):
    sum=sum+a[i]
print(sum)    
            
