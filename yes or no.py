str=input()
try:
    float(str)
    print("yes")
except ValueError:
    print("no")
