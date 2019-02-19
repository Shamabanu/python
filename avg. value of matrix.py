num = int(input())
s = 0
for j in range(0,num):
    tem = list(map(int,input().split()))
    s = s+ sum(tem)
count = num*num
a = s/count
print("{0:.6f}".format(round(a,6)))
