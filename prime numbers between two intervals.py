Lower,Upper=input().split()
Lower=int(Lower)
Upper=int(Upper)
for num in range(Lower+1,Upper):
   if(num > 1):
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
