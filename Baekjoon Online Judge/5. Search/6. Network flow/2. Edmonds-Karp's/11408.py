# 11408: 열혈강호 5
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f = 1, c = 0):
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0
    cost[u][v] = c
    cost[v][u] = -c

n, m = map(int, input().split())
node = n + m + 2
capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]
cost = [dict() for _ in range(node)]

for i in range(1, n + 1):
    link(0, i, 1)
for i in range(n + 1, node - 1):
    link(i, node - 1, 1)
for i in range(1, n + 1):
    work = list(map(int, input().split()))
    for j in range(1, work[0] + 1):
        link(i, work[j * 2 - 1] + n, INF, work[j * 2])

min_work = 0
min_cost = 0
while 1:
    visit = [-1] * node
    is_inQ = [0] * node
    dist = [INF] * node

    spfa = deque([0])
    is_inQ[0] = 1
    dist[0] = 0

    while spfa:
        now = spfa.popleft()
        is_inQ[now] = 0

        for next in capa[now]:
            if capa[now][next] - flow[now][next] > 0 and dist[next] > dist[now] + cost[now][next]:
                dist[next] = dist[now] + cost[now][next]
                visit[next] = now
                if is_inQ[next] == 0:
                    is_inQ[next] = 1
                    spfa.append(next)

    if visit[node - 1] == -1:
        break

    f = INF
    r = node - 1
    while r:
        f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
        r = visit[r]

    r = node - 1
    while r:
        min_cost += f * cost[visit[r]][r]
        flow[visit[r]][r] += f
        flow[r][visit[r]] -= f
        r = visit[r]
    min_work += f

print(min_work)
print(min_cost)