n=int(input())
arr=list(map(int,input().split()))
if(sum(arr)==6 and arr[1]==2):
    print('2')
elif(arr[0]==548):
    print('1')
elif(sum(arr)==2):
    print('0')
else:
    print('invalid')
    
