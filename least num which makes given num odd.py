num=int(input())
for i in range(1,num):
    m=int(num/i)
    if(m%2!=0 and num%i==0):
        print(i)
        break
else:
    print(num)
