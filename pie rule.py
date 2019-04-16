a = int(input())
Np = [0] + [ int(x) for x in input().split()]
Nsum = [0 for i in range(0,a+4)]
np = 2
A = 0
B = 1
Nmax = []
for i in range(0,a+1) :
    Nmax.append([0,0])

for i in range(a,0,-1) :
    Nsum[i] = Np[i] + Nsum[i+1]
    if i == a :
        Nmax[i][A] = Nmax[i][B] = Np[i]
    else :
        Nmax[i][A] = max(Nmax[i + 1][A], Np[i] + Nsum[i + 1] - Nmax[i + 1][B])
        Nmax[i][B] = max(Nmax[i + 1][B], Np[i] + Nsum[i + 1] - Nmax[i + 1][B])
Amax = Nsum[1] - Nmax[1][B]
print(Amax, Nmax[1][B])
