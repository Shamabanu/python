n=int(input())
s=input().split()
s.sort() 
max = 1; res = s[0]; cur = 1
for i in range(1, n):  
    if (s[i] == s[i - 1]): 
        cur += 1
              
    else : 
        if (cur > max):  
            max = cur 
            res = s[i - 1] 
              
        curr_count = 1

if (cur > max): 
      
    max = cur 
    res = s[n - 1] 
print(res) 
