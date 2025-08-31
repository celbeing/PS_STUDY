# 2247: 실질적 약수
import sys
input = sys.stdin.readline

res = 0
n = int(input())
for i in range(2, n // 2 + 1):
    res += (n // i - 1) * i

res %= 1000000
print(res)