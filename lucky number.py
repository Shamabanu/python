p=int(input())
l=input().split()
m=[]
for i in range(0,len(l)):
    m.append(int(l[i]))
    if((i+1)*m[i]==m[i]):
        print(m[i])
        break
else:
    print("0")
