n=input()
sum=0
for i in range(0,len(n)):
    if(n[i].isdigit() or n[i].isalpha() or n[i]==" "):
        sum=sum
    else:
        sum=sum+1
print(sum)
