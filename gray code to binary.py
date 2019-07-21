n=int(input())
n=int(n,2)
m=n
while(m!=0):
  m=(m>>1)
  n^=m
print(bin(n)[2::])
