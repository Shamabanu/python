h,j=map(str,input().split())
co=0
for x in range(0,len(h)):
    c=h[x]
    d=j[x]
if(c==d):
        co=co
else:
    co=co+1
if(co==1):
            print("yes")
else:
    print("no")
