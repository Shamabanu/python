m,n=input().split()
if(m.isdigit() and n.isdigit()):
              m,n=int(m),int(n)
              if(n==1):
                  print("1 2")
              else:
                 print("1 "+str(m-n))
