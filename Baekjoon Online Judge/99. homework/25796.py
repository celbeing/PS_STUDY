# 25796: 초콜릿 나눠 팔기
import sys
input = sys.stdin.readline
mod = int(1e9 + 7)
dp = [0] * 50001
dp[0] = 1
dp[1] = 3
prefix_sum = 0
for i in range(2, 50001):
    prefix_sum += dp[i - 1] << 1
    prefix_sum %= mod
    dp[i] = (prefix_sum + dp[i - 1] + 2) % mod

for _ in range(int(input())):
    n, r, c = map(int, input().split())
    if (r + c) & 1:
        print(0)
        continue
    elif r == 2:
        res = dp[(c >> 1) - 1] * dp[(n - c) >> 1] * 2
        print(res)
    else:
        break