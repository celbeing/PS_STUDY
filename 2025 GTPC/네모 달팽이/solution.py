dp = [0] * 38
dp[0] = 1
dp[1] = 2
dp[2] = 3
for i in range(3, 38):
    dp[i] = dp[i - 2] + dp[i - 3] + 1
shell = [0] * 38
shell[2] = 1
for i in range(3, 38):
    shell[i] = shell[i - 1] + dp[i - 3] ** 2

n = int(input())
if n == 1: print(1)
else: print((dp[n] - 1) * (dp[n - 1]) - shell[n])