n=list(map(int,input().split()))
n=sorted(n)
if(n[0]+n[1]>n[2]):
    print("yes")
else:
    print("no")
