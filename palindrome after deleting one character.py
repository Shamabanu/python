s1=input()

for j in range(0,len(s1)):
    k=s1[:j]+s1[j+1:]

    if(k[:]==k[::-1]):
    
        print("YES")
        break
else:
    print("NO")
