num=list(input())
s=[]
for i in num:
  if(int(i)%2!=0):
    s.append(int(i))
if(sum(s)%2==0):
  print("E")
else:
  print("O")
