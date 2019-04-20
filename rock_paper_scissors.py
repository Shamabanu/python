s1,s2=map(str,input().split())
if (s1=="R" and s2=="P") or (s1=="P" and s2=="R"):
    print("P")
elif (s1=="S" and s2=="R") or (s1=="R" and s2=="S"):
    print("R")
elif s1==s2:
    print("D")
else:
    print("S")
