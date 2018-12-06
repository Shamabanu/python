n = int(input())
arr = input()   
l = list(map(int,arr.split(' ')))
m = sorted(l)
i = n/2
p = int(i)
print(m[p])
