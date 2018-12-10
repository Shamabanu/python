n=int(input())
arr=input().split()
arr.sort() 
max = 1; res = arr[0]; cur = 1
for i in range(1, n):  
    if (arr[i] == arr[i - 1]): 
        cur += 1
              
    else : 
        if (cur > max):  
            max = cur 
            res = arr[i - 1] 
              
        curr_count = 1

if (cur > max): 
      
    max = cur 
    res = arr[n - 1] 
print(res) 
