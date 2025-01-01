# 12784: 인하니카 공화국
import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    inf = int(1e9)
    for _ in range(int(input())):
        n, m = map(int, input().split())
        brdg = [dict() for _ in range(n + 1)]
        for _ in range(m):
            u, v, d = map(int, input().split())
            brdg[u][v] = d
            brdg[v][u] = d
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)
        cost = [0] * (n + 1)
        depth[1] = -1
        bfs = deque([1])
        bomb = []
        while bfs:
            now = bfs.popleft()
            if len(brdg[now]) == 1:
                heappush(bomb, (depth[now], now))
                cost[now] = inf
            for next in brdg[now]:
                if depth[next]: continue
                bfs.append(next)
                depth[next] = depth[now] - 1
                parent[next] = now
        cost[1] = 0
        while bomb:
            dep, now = heappop(bomb)
            if now == 1: break
            if cost[parent[now]] == 0: heappush(bomb, (dep + 1, parent[now]))
            cost_p = brdg[now][parent[now]]
            cost[parent[now]] += min(cost[now], cost_p)
        print(cost[1])
solution()