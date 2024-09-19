#2688: 줄어들지 않아
import sys
input = sys.stdin.readline
def solution():
    dp = [[0] * 65 for _ in range(10)]
    dp[0][0] = 1
    res = [0] * 65
    for j in range(1, 65):
        for i in range(10):
            for k in range(i + 1):
                dp[i][j] += dp[k][j - 1]
            res[j] += dp[i][j]
    for _ in range(int(input())):
        print(res[int(input())])
solution()