M=input()
N=input()
start = 0
while start < min(len(M), len(N)):
    if M[start] != N[start]:
        break
    start += 1
print(M[:start])
