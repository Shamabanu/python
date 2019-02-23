num=(input())
arr=[]
for x in num:
    if(x not in arr):
        arr.append(x)
arr="".join(arr)
if(num==arr):        
    print("no")
else:
    print("yes")
