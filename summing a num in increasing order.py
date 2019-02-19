num=input()
m=0
for i in range(0,len(num)):
    for j in range(0,i+1):
        m=m+int(num[j])
print(m)
