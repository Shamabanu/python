def multiple(N):  
    a = range(N, (5 * N)+1, N) 
    print(*a)  
N = int(input())
multiple(N)
