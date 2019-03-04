num = int(input())
m = 0
k = 0
while(k<num):
    k=2**m
    m+=1
if(k==num):
    print("yes")
else:
    print("no")
