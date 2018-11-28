s=input()
try:
    float(s)
    print("Yes")
except ValueError:
    print("No")
