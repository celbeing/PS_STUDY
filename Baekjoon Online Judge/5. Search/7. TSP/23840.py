# 23840: 두 단계 최단 경로 4
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = int(1e14)

n, m = map(int, input().split())
link = [dict() for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    link[u][v] = w
    link[v][u] = w
x, z = map(int, input().split())
p = int(input())
node = list(map(int, input().split()))
p_connect = dict()
p_connect[x] = 0
p_connect[z] = p + 1
for i in range(1, p + 1):
    p_connect[node[i - 1]] = i

distance = [[-1] * (p + 2) for _ in range(p + 2)]

for i in p_connect:
    bfs = []
    heappush(bfs, (0, i))
    reach = [inf] * (n + 1)
    reach[i] = 0
    while bfs:
        dist, now = heappop(bfs)
        if reach[now] < dist: continue
        for next in link[now]:
            new_dist = dist + link[now][next]
            if new_dist < reach[next]:
                reach[next] = new_dist
                heappush(bfs, (new_dist, next))
    for j in p_connect:
        if i == j: continue
        if reach[j] == inf:
            print(-1)
            exit()
        else:
            distance[p_connect[i]][p_connect[j]] = reach[j]

x, z = 0, p + 1

dp = [[0] * (1 << z) for _ in range(z)]
for i in range(1, z):
    dp[i][(1 << z) - 1] = distance[i][z]

def TSP(now, visit):
    if dp[now][visit] == 0:
        dp[now][visit] = inf
        for next in range(1, z):
            if visit & 1 << next: continue
            dp[now][visit] = min(dp[now][visit], TSP(next, visit | 1 << next) + distance[now][next])
    return dp[now][visit]

print(TSP(0, 1))