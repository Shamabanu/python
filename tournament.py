num=int(input())
if(num>0 and (num & (num-1))==0):
    print("0")
else:
    if(num%2!=0):
        print("1")
    else:
        print("2")
