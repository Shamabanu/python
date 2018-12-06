s=input()
try:
    float(s)
    print("yes")
except ValueError:
    print("no")
