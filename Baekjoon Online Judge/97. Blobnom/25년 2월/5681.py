# 5681: 공 쌓기
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    while True:
        n = int(input())
        if n == 0: break
        prefix = []
        for i in range(n):
            prefix.append(list(map(int, input().split())))
            for j in range(i):
                prefix[i][j] += prefix[i - 1][j]
        dp = [[0] * n for _ in range(n)]
        hq = []
        for i in range(n):
            dp[i][0] = prefix[i][0]
            heappush(hq, (-prefix[i][0], i))
        result = -hq[0][0]
        if result < 0: result = 0
        for j in range(1, n):
            for i in range(j, n):
                while hq[0][1] < i - 1:
                    heappop(hq)
                dp[i][j] = prefix[i][j] - hq[0][0]
                if result < dp[i][j]:
                    result = dp[i][j]
            hq.clear()
            for i in range(j, n):
                heappush(hq, (-dp[i][j], i))
        print(result)
    return
solution()