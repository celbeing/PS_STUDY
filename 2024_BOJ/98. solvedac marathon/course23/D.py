#1695: 팰린드롬 만들기
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * N
    dp2 = [0] * N
    for k in range(1, N):
        i = N - k - 1
        for j in range(N - 1, k - 1, -1):
            dp2[j] = dp[j]
            if arr[i] == arr[j]:
                dp[j] = dp2[j - 1]
            else:
                dp[j] = min(dp[j], dp[j - 1]) + 1
            i -= 1
    print(dp[-1])
solution()