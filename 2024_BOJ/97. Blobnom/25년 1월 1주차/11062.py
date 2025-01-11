# 11062: 카드 게임
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n = int(input())
        cards = list(map(int, input().split()))
        dp = [[0] * n for _ in range(n)]
        t = n & 1
        for i in range(n):
            for j in range(n - i):
                if i == 0:
                    dp[j][i + j] = cards[j] if t else 0
                elif t:
                    dp[j][i + j] = max(dp[j + 1][i + j] + cards[j], dp[j][i + j - 1] + cards[i + j])
                else:
                    dp[j][i + j] = min(dp[j + 1][i + j], dp[j][i + j - 1])
            t ^= 1
        print(dp[0][-1])
solution()