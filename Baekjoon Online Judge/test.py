dp = [0] * 73
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 73):
    dp[i] = dp[i - 2] + dp[i - 3] + 1
print()