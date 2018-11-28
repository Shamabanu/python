Num = int(input())
if Num > 1:

   for i in range(2,Num):
       if (Num % i == 0):
           print("no")
           break
   else:
       print("yes")
    
else:
   print("no")
