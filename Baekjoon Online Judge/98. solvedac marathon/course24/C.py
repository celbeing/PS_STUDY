#1660: 캡틴 이다솜
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    dp = [300000] * 300001
    dp[0] = 0
    k = 1
    t = k
    for i in range(2, 122):
        k += i
        for j in range(t, 300001):
            if dp[j] > dp[j - t] + 1:
                dp[j] = dp[j - t] + 1
        t += k
    print(dp[N])
solution()