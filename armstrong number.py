N = (input())
arm_num = 0
v = int(N)
while(v > 0):
    
    reminder=v % 10
    arm_num += reminder ** 3
    v //= 10
if int(N) == arm_num:
        print("yes")
else:
        print("no")

