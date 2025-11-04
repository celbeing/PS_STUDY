# 2718: 타일 채우기
import sys
input = sys.stdin.readline

dp = [0] * 22
dp[0] = 1
dp[1] = 1
pf_even = 1
pf_odd = 1

for i in range(2, 22):
    dp[i] = dp[i - 2] + (pf_odd if i & 1 else pf_even) * 3 + (pf_even if i & 1 else pf_odd) * 2 - dp[i - 1]
    if i & 1: pf_odd += dp[i]
    else: pf_even += dp[i]

for _ in range(int(input())):
    print(dp[int(input())])