p=input().split()
m=int(p[1])
n=str(p[0])
for i in range(0,len(n)-m+1):
    if(i<len(n)-m):
        for j in range(i,i+m):
            if(j<i+m-1):
                print(n[j],end=(""))
            else:
                print(n[j],end=(" "))
    else:
        for j in range(i,i+m):
            if(j<i+m-1):
                print(n[j],end=(""))
            else:
                print(n[j],end=(""))
