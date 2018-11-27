N=int(input())
C=0
while(N>0):
    dig=N%10
    C=C+dig
    N=N//10
print(C)    
