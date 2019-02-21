import collections
S =input()
fr = collections.Counter(S)
max = 0
for k,v in fr.items():
    if(v > max):
        tem = k
        max = v
print(tem)
