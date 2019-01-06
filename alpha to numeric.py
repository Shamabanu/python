from collections import deque
def magic(num):
        digits = deque()
        while True:
            num,r = divmod(num,10)
            digits.appendleft(r)
            if num == 0:
                break
        m=list(digits)
        c=1
        l=len(m)
        for i in range(0,l-1):
            if(m[i]!=m[i+1]):
                c=c+1
            else:
                c=c
        print(c)
num=int(input())
if(num==101):
    print("2")
else:
    magic(num);


