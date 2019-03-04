num = bin(int(input()))
num = str(num)
k = 0
for x in num:
    if(x == '1'):
        k+=1
print(k)
