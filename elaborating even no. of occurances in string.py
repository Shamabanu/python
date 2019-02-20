s=input()
n=''
for x in range(0,len(s)-1,2):
  if int(s[x+1])%2==0:
    n+=s[x]*int(s[x+1])
  else:
    n+=s[x]+s[x+1]
print(n)
