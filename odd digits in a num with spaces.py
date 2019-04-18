n=(input())
a=[]
for i in n:
    a.append(i)
for i in range(0,len(n)):
    if(int(a[i])%2!=0):
        print(a[i],end=" ")

