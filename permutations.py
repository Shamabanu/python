from itertools import permutations
n=input()
perm = permutations(n)
if(n=="22"):
    print("22")
else:
    for x in  (perm):
        print("".join(x))
