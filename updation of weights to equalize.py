s1=(input())
k1=(input())
s1=list(s1.split("|"))
if len(s1[0])==len(s1[1]):
    print("Impossible")
if len(s1[1])<len(s1[0]):
    if len(s1[1])+len(k1)==len(s1[0]):
        m=""
        s1[1]=s1[1]+k1
        m=m+s1[0]+"|"+s1[1]
        print(m)
    else:
        print("Impossible")
if len(s1[0])<len(s1[1]):
    if len(s1[0])+len(k1)==len(s1[1]):
        m=""
        s1[0]=s1[0]+k1
        m=m+s1[0]+"|"+s1[1]
        print(m)
    else:
        print("Impossible")
