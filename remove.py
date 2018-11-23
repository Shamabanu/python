p=input()
n=""
k=len(p)
m="".join(reversed(p))
vowels=('a','e','i','o','u')
for x in m.lower():
    if x in vowels:
        n=m.replace(x,"")
        print(n)
