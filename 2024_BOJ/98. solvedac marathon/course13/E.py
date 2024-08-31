#9764: 서로 다른 자연수의 합
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    peek = 0
    for i in range(1,N+1):
        peek += i
        for j in range(N+1):
            if j > peek: break
            dp[i][j] = dp[i-1][j]
            if j >= i: dp[i][j] += dp[i-1][j-i]
            dp[i][j] %= 100999
    print(dp[-1][-1])