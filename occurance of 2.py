num=int(input())
sum=0
for i in range(0,num+1):
    p=str(i)
    sum+=p.count('2')
print(sum)
