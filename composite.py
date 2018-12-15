str = int(input())
if str > 1:
    for i in range(2,str):
       if (str % i) == 0:
           print("yes")
           break
    else:
       print("no")
else:
   print("yes")
