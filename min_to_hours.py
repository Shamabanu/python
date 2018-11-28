Len=int(input())
if(Len > 0):
    Len = "%d %02d" % (Len / 60, Len % 60)
else:
    Len = ""
print(Len)
