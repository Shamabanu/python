num=int(input())
sh=0
for i in range(1,num+1):
    if(i%2!=0 and i%10==3):
        sh=sh+i
print(sh)
