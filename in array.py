n=int(input())
a=input().split()
a.sort() 
max = 1; res = a[0]; cur = 1
for i in range(1, n):  
    if (a[i] == a[i - 1]): 
        cur += 1
              
    else : 
        if (cur > max):  
            max = cur 
            res = a[i - 1] 
              
        curr_count = 1

if (cur > max): 
      
    max = cur 
    res = a[n - 1] 
print(res) 
