num=input().split()
if(len(num)==1):
    print(num[0])
else:
    for i in range(0,len(num)):
        if(num[i]=='and'):
            num[i-1],num[i+1]=num[i+1],num[i-1]
    s=" ".join(map(str,num))
    print(s)
