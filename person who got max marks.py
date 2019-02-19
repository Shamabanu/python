person1,mark11,mark12,mark13 = map(str,input().split('#'))
person2,mark21,mark22,mark23 = map(str,input().split('#'))
s1 = int(mark11)+int(mark12)+int(mark13)
s2 = int(mark21)+int(mark22)+int(mark23)
if(s1>=s2):
    print(person1)
else:
    print(person2)
