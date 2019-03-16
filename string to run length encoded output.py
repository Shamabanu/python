string=input()
string = list(string)
s = []
l = string[0]
count = 1
for x in range(1,len(string)):
    if(string[x] == l):
        count += 1
    else:
        s.append(l)
        s.append(str(count))
        l = string[x]
        count = 1
s.append(l)
s.append(str(count))
print( ''.join(s))


