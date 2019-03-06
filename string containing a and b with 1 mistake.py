s=str(input())
if(len(s)==(s.count('a')+s.count('b')+1)):
    print("yes")
elif(len(s)==(s.count('a')+s.count('b'))):
    print("yes")
else:    
    print("no")
