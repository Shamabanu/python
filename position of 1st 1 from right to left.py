num = bin(int(input()))
num = str(num)
m = num.rfind('1')
s = len(num)
print(s-m)
#rfind() returns the highest index of the substring if found in given string
