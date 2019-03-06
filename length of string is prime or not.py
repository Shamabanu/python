s=input()
k="".join(s)
p=len(k)
for i in range(2,p):
    if(p%i==0):
        print("no")
        break
else:
    print("yes")
