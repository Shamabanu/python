n = (input())
arm_num = 0
val = int(n)
while val > 0:
    
    reminder=val % 10
    arm_num += reminder ** 3
    val //= 10
if int(n) == arm_num:
        print("yes")
else:
        print("no")

