a = str(input())
max = 0
m = a[0]
c = 1
ans = m
for i in range(1,len(a)):
    if(a[i] == m):
        c+=1
        if(c > max):
            max = c
            ans = a[i]
    else:
        c = 1
        m = a[i]
    
print(ans,max)
