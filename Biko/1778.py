# 1778: 계단
m, f, n = map(int, input().split())
res = n // (m - 1)
if n % (m - 1): res += 1
print(res)