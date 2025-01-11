import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        b[i] += b[i - 1]
    inf = max(a[-1], b[-1])
    a_dp = [a[-1]] * (n + 1)
    b_dp = [b[-1]] * (n + 1)
    a_dp[0] = 0
    b_dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            ta = a[j] - a[i - 1]
            tb = b[j] - b[i - 1]
            a_dp[j - i + 1] = min(a_dp[j - i + 1], ta)
            b_dp[j - i + 1] = min(b_dp[j - i + 1], tb)
    res = inf
    for i in range(n + 1):
        j = 2 * n - k - i
        if 0 <= j <= n:
            res = min(res, max(a_dp[i], b_dp[j]))
    print(res)
solution()
