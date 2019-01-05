def asciitoindex(n):
    return ord(n)-96
try:
    s1=str(input())
    s2=str(input())
    s1=s1.lower()
    s2=s2.lower()
    nr=[]
    s=1
    for i,j in zip(s1,s2):
        if s%2==0:
            nr.append(chr((asciitoindex(j)+asciitoindex(i))%27 +int((asciitoindex(j)+asciitoindex(i))/27)+96))
        else:
            nr.append(chr((asciitoindex(i)+asciitoindex(j))%27 +int((asciitoindex(j)+asciitoindex(i))/27)+96))
        s+=1
    print("".join(nr))
except:
    pass
