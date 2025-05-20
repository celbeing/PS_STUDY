# 10573: 증가하는 수
import sys
input = sys.stdin.readline
def solution():
    dp = [[0] * 10 for _ in range(82)]
    for i in range(1, 10): dp[1][i] = 1
    for i in range(1, 82):
        for j in range(10):
            for k in range(j, -1, -1):
                dp[i][k] += dp[i - 1][j]
    for _ in range(int(input())):
        n = list(input().strip())
        k = len(n)
        flag = False
        for i in range(1, k):
            if int(n[i - 1]) > int(n[i]):
                flag = True
                break
        if flag:
            print(-1)
            continue
        res = dp[k + 1][0]
        for i in range(k):
            for j in range(int(n[i]) + 1, 10):
                res -= dp[k - i][j]
        print(res)
solution()