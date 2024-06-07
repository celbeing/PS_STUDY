import sys
input = sys.stdin.readline
inf = int(1e9)
N = int(input())
W = list(map(int,input().split()))
M = int(input())
L = list(map(int,input().split()))
K = int(input())

dp = [[-inf]*(M+1) for _ in range(N+M+1)]
dp[0][0] = 0
for i in range(1,N+M+1):
    if i <= N: dp[i][0] = dp[i-1][0]+W[i-1]
    for j in range(1,M+1):
        if j > i: break
        if i-j > N: continue
        win = dp[i-1][j] + W[i-j-1]
        b = dp[i-1][j-1] % K
        if b == 0:
            b = L[j-1]
        elif b > L[j-1]:
            b = L[j-1]
        lose = dp[i-1][j-1] - b
        if win > lose:
            dp[i][j] = win
        else:
            dp[i][j] = lose
print(dp[N+M][M])