n,m = input().split()
p,q = len(n),len(m)
if(p%q == 0 or q%p == 0):
    print('no')
else :
    print('yes')
