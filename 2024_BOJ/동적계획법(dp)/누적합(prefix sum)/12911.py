#12911 좋아하는 배열
N,K = map(int,input().split())
div = int(1e9+7)
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
sum = [0 for _ in range(N+1)]
for i in range(1,K+1): dp[1][i] = 1
sum[1] = K

for i in range(2, N+1):
    for j in range(1, K+1):
        dp[i][j] += sum[i-1]
        for k in range(j*2,K+1, j):
            dp[i][j] -= dp[i-1][k]
        sum[i] += dp[i][j]
        sum[i] %= div

print(sum[N]%div)