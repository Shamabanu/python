m,s=map(int,input().split())
arr=input().split()
l=[]
for x in arr:
    l.append(int(x))
l.sort()
for x in range(0,len(l)):
    if(s==l[x]):
        if(x==0):
            print(l[x+1],l[x+2],l[x+3],sep=' ')
        if(x==len(l)-1):
            print(l[x-1],l[x-2],l[x-3],sep=' ')
        if(x>1 and x<len(l)-2):
            print(l[x-1],l[x+1],l[x-2],sep=' ')
        if(x==1):
            print(l[x-1],l[x+1],l[x+2],sep=' ')
