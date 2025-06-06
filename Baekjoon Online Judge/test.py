n = int(input())
dp = [0] * (n + 1)
dp[0] = 1

prime = []
sieve = [0] * (n + 1)
for i in range(2, n + 1):
    if sieve[i]: continue
    prime.append(i)
    for j in range(i * i, n + 1, i):
        sieve[j] = 1

for p in prime:
    for i in range(p, n + 1):
        dp[i] += dp[i - p]
        dp[i] %= 1_000_000_007

print(dp[-1])