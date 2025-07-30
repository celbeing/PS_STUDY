# 2043: 수 묶기
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def link(u, v, f, c):
    capa[u][v], capa[v][u] = f, 0
    flow[u][v], flow[v][u] = 0, 0
    cost[u][v], cost[v][u] = c, -c
    return

n, m, t = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

source = n * m
sink = source + 1
node = sink + 1

capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]
cost = [dict() for _ in range(node)]

for i in range(n):
    for j in range(m):
        now = i * m + j
        link(source, now, 1, 0)
        link(now, sink, 1, 0)
        if (i + j) & 1: continue
        for k in range(4):
            di, dj = i + d[k][0], j + d[k][1]
            if 0 <= di < n and 0 <= dj < m:
                side = di * m + dj
                gap = abs(nums[i][j] - nums[di][dj])
                if gap > t: link(now, side, 1, INF)
                else: link(now, side, 1, -gap)

res = 0
while 1:
    visit = [-1] * node
    is_inQ = [0] * node
    dist = [INF] * node

    spfa = deque([source])
    is_inQ[source] = 1
    dist[source] = 0

    while spfa:
        now = spfa.popleft()
        is_inQ[now] = 0
        for next in capa[now]:
            if capa[now][next] - flow[now][next] > 0 and dist[next] > dist[now] + cost[now][next]:
                dist[next] = dist[now] + cost[now][next]
                visit[next] = now
                if is_inQ[next] == 0:
                    spfa.append(next)
                    is_inQ[next] = 1

    if visit[sink] == -1: break

    r = sink
    total = 0
    while r != source:
        total -= cost[visit[r]][r]
        flow[visit[r]][r] += 1
        flow[r][visit[r]] -= 1
        r = visit[r]
    if total < 0: break
    res += total

print(res)