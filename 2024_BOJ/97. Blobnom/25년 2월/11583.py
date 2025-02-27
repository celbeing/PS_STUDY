# 11583: 인경호의 징검다리
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = list(map(int, input().split()))
        factor = [[0, 0] for _ in range(n)]
        for i in range(n):
            a = s[i]
            while a % 2 == 0:
                a //= 2
                factor[i][0] += 1
            while a % 5 == 0:
                a //= 5
                factor[i][1] += 1
        dp = [[0, 0] for _ in range(n)]
        dp[0] = factor[0]
        