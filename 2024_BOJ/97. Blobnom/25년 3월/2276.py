# 2276: 물 채우기
import sys
sys.setrecursionlimit(int(1e6))
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    m, n = map(int, input().split())
    bottle = [list(map(int, input().split())) for _ in range(n)]
    check = [[0] * m for _ in range(n)]
    low = []
    for i in range(n):
        heappush(low, (bottle[i][0], i, 0))
        heappush(low, (bottle[i][-1], i, m - 1))
        check[i][0] = 1
        check[i][-1] = 1
    for i in range(1, m - 1):
        heappush(low, (bottle[0][i], 0, i))
        heappush(low, (bottle[-1][i], n - 1, i))
        check[0][i] = 1
        check[-1][i] = 1
    def dfs(x, y, h):
        res = 0
        for k in range(4):
            nx, ny = x + d[k][0], y + d[k][1]
            if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 0:
                check[nx][ny] = 1
                if bottle[nx][ny] > h:
                    heappush(low, (bottle[nx][ny], nx, ny))
                else:
                    res += h - bottle[nx][ny]
                    res += dfs(nx, ny, h)
        return res
    res = 0
    while low:
        h, x, y = heappop(low)
        res += dfs(x, y, h)
    print(res)
solution()