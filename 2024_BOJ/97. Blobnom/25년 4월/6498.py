# 6498: 앨리어스 감마 코드
import sys
input = sys.stdin.readline
def solution():
    inf = int(1e9)
    while True:
        n = int(input())
        if n == 0: break
        dp = [[inf] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        c = [0] + list(map(int, input().split()))
        for i in range(1, n + 1):
            pass
        # 이게 왜 골드 4임..?