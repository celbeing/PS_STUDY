import sys
input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0: break
    dp = [0]*N
    dp[0] = int(input())
    high = -int(1e10)
    if dp[0] > high: high = dp[0]
    for i in range(1,N):
        k = int(input())
        if dp[i-1]+ k > k:
            dp[i] = dp[i-1]+k
        else:
            dp[i] = k
        if dp[i] > high:
            high = dp[i]
    print(high)