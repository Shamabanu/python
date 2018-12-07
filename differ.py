h,j=map(str,input().split())
count=0
for x in range(0,len(h)):
    c=h[x]
    d=j[x]
if(c==d):
        count=count
else:
    count=count+1
if(count==1):
            print("yes")
else:
    print("no")
