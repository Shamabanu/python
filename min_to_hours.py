len=int(input())
if len > 0:
    len = "%d:%02d" % (len / 60, len % 60)
else:
    len = ""
print(len)
