def freq(n, k, b, N):
    diff = (sum(N) - N[k]) / 2
    if b == diff:
        return 'Bon Appetit'
    else:
        return str(N[k] // 2)


n, k = map(int, input().split())
N = list(map(int, input().split()))
b = int(input())
res = freq(n, k, b, N)
print(res)
