m1 = input()
m2 = input()
s = m1.split()
s2 = [ x for x in s if x != m2]
print(*s2)
