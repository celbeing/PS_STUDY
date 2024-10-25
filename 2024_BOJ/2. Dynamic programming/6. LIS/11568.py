#11568: 민균이의 계략
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    card = list(map(int, input().split()))
    dp = [1] * n
    high = 1
    for i in range(1, n):
        for j in range(i):
            if card[i] > card[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                high = max(high, dp[i])
    print(high)
solution()