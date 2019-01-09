s=input()
arr=[]
for x in s:
    if(x not in arr):
        arr.append(x)
n=''.join(arr)
print(n)

