N=int(input())
S=input()
P="".join(reversed(S))
for i in "aeiouAEIOU":
    P=P.replace(i,"")
print(P)
