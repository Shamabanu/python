st=str(input())
arr=[]
d=['d','h','o','n','i']
d.sort()
for x in st:
    arr.append(x)
arr.sort()
if(d==arr):
    print("yes")
else:
    print("no")
