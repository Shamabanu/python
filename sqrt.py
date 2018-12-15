import math
m,s=map(int,input().split())
s=m * s
if math.sqrt(s).is_integer():
    print ("yes")
else:
    print ("no")
