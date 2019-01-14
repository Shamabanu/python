n=input()
sum=0
for x in range(0,len(n)):
    if(n[x].isdigit()):
        sum=sum+1
    else:
        sum=sum
print(sum)

