import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
for i in range(1,N+1):
    A,B,C,D = map(int,input().split())
    up = dp[i-1]+B
    down = 0
    F = C+D
    if dp[i-1]%F < C:
        down = dp[i-1]+A
    else:
        down = dp[i-1] + F - dp[i-1] % F + A
    if up < down: dp[i] = up
    else: dp[i] = down
print(dp[-1])