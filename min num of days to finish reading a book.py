num,s=map(int,input().split())
lis=list(map(int,input().split()))
count=0
for x in lis:
  time_remain=86400-x
  s=s-time_remain
  count+=1
  if(s<=0):
    break
print(count)
