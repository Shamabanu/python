p,q=input().split(' ')
for j in range(len(p)):
   if(j<len(p)-1): 
      if(p[j]+p[j+1] in q):
         print("yes")
         break
else:
    print("no")
