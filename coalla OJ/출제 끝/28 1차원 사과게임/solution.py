import sys
from collections import deque
input = sys.stdin.readline

def solution(n, a):
    s = [0] * n
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i - 1] + a[i]

    count = [[-1] * n for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    for i in range(n): count[i][i] = 0

    def pf(i, j):
        return s[j] - s[i] + a[i]

    def dfs(i, j):
        if count[i][j] == -1:
            if pf(i, j) == 10:
                count[i][j] = 10
                dp[i][j] = j - i + 1
                return count[i][j]

            count[i][j] = 0
            prefix_sum = pf(i, j)
            for k in range(i, j):
                left = count[i][k] if count[i][k] > -1 else dfs(i, k)
                right = count[k + 1][j] if count[k + 1][j] > -1 else  dfs(k + 1, j)
                l_dp = dp[i][k]
                r_dp = dp[k + 1][j]
                if prefix_sum == left + right:
                    count[i][j] = prefix_sum
                    dp[i][j] = l_dp + r_dp
                    break
                elif prefix_sum - (left + right) == 10:
                    count[i][j] = prefix_sum
                    dp[i][j] = j - i + 1
                    break
                elif dp[i][j] < l_dp + r_dp:
                    count[i][j] = count[i][k] + count[k + 1][j]
                    dp[i][j] = l_dp + r_dp
        return count[i][j]

    dfs(0, n - 1)
    print(dp[0][-1])
    return dp[0][-1]