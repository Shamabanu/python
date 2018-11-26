m=input()
n=input()
start = 0
while start < min(len(m), len(n)):
    if m[start] != n[start]:
        break
    start += 1
print(m[:start])
