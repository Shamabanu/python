s=input()
m=[]
for i in s:
    if(i not in m):
        m.append(i)
if(len(m)==27 or len(m)==28):
    print("yes")
else:
    print("no")
