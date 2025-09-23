import sys

input = sys.stdin.readline
mod = int(1e9 + 7)
dp1 = [0] * 50001
dp2 = [0] * 50001
dp1[0], dp2[0] = 1, 1
ps1, ps2 = 1, 1
for i in range(1, 50001):
    dp1[i] = dp1[i - 1] + ps1 * 2
    ps1 += dp1[i]

    dp2[i] = dp2[i - 1] + ps2 * 2 + 1
    ps2 += dp2[i]
print()