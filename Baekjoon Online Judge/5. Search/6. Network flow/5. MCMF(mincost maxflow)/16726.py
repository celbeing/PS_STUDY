# 16726: 영과일 학회방
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def link(u, v, c = 0):
    capa[u][v], capa[v][u] = 1, 0
    flow[u][v], flow[v][u] = 0, 0
    cost[u][v], cost[v][u] = c, -c
    return

n, m = map(int, input().split())
ground = [list(input().strip()) for _ in range(n)]
source = n * m
sink = source + 1
node = sink + 1

capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]
cost = [dict() for _ in range(node)]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 'X': continue
        now = i * m + j
        link(source, now)
        link(now, sink)
        if (i + j) & 1: continue
        for k in range(4):
            di, dj = i + d[k][0], j + d[k][1]
            if 0 <= di < n and 0 <= dj < m and ground[di][dj] == '.':
                side = di * m + dj
                link(now, side, -1)

tile = 0
while 1:
    is_inQ = [0] * node
    visit = [-1] * node
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

    c, r = 0, sink
    while r != source:
        flow[visit[r]][r] += 1
        flow[r][visit[r]] -= 1
        c -= cost[visit[r]][r]
        r = visit[r]
    if c < 0: break
    tile += 1

print(tile)