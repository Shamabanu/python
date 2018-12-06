N = int(input())
a = input()
l = list(map(int,a.split(' ')))
for i in range(0,N):
    print(l[i], i )
