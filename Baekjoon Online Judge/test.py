n = int(input())
if n in (1, 3): print(-1)
else:
    dp = [int(1e9) if i & 1 else i // 2 for i in range(n + 1)]
    for i in range(5, n + 1):
        dp[i] = min(dp[i], dp[i - 5] + 1)
    print(dp[n])