N=int(input())
a=[]
a=list(map(int,input().split()))
s1=a[::2]
s2=a[1::2]
s3=a[1::3]
if(sum(s1)>sum(s2) and sum(s1)>sum(s3)):
  print(sum(s1))
elif(sum(s3)>sum(s1) and sum(s3)>sum(s2)):
  print(sum(s3))
else:
    print(sum(s2))
