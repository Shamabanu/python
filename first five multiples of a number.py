def multiple(n):  
    a = range(n, (5 * n)+1, n) 
    print(*a)  
n = int(input())
multiple(n)
