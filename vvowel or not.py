m=(input())
arr='aeiouAEIOU'
n=len(m)
k=0
for i in range(0,n):
    if(m[i] in arr):
        k=k+1
    else:
        k=k
if(k>0):
    print("yes")
else:
    print("no")
    
