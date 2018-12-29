S=list(map(int,(input()).split()))
b=sorted(list(map(int,(input()).split())))[::-1]
M=0
for j in range(len(b)):
  if(S[1]>=b[j]):
    M+=int(S[1]/b[j])
    S[1]%=b[j]
if(S[1]==0):
  print(M)
else:
  print("not possible")
