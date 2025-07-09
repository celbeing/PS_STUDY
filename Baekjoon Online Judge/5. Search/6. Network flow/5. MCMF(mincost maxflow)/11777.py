# 11777: 남욱이의 썩은 계란판
import sys
from collections import deque
from heapq import heappush, heappop, heappushpop
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f = 1, c = 0):
    capa[u][v], capa[v][u] = f, 0
    flow[u][v], flow[v][u] = 0, 0
    cost[u][v], cost[v][u] = c, -c

n, k = map(int, input().split())
rot = [list(map(int, input().split())) for _ in range(n)]
total = 0
for i in range(n):
    total += sum(rot[i])

node = n * n + 3
s, t = node - 2, node - 1
capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]
cost = [dict() for _ in range(node)]

link(s, s - 1, k, 0)
candidate = []
for i in range(node - 3):
    x, y = i // n, i % n
    if (x + y) & 1: continue
    c = rot[x][y]
    if len(candidate) > k << 3:
        if x and candidate[0][0] < rot[x - 1][y] + c:
            heappushpop(candidate, (rot[x - 1][y] + c, i, i - n))
        if x < n - 1 and candidate[0][0] < rot[x + 1][y] + c:
            heappushpop(candidate, (rot[x + 1][y] + c, i, i + n))
        if y and candidate[0][0] < rot[x][y - 1] + c:
            heappushpop(candidate, (rot[x][y - 1] + c, i, i - 1))
        if y < n - 1 and candidate[0][0] < rot[x][y + 1] + c:
            heappushpop(candidate, (rot[x][y + 1] + c, i, i + 1))
    else:
        if x:
            heappush(candidate, (rot[x - 1][y] + c, i, i - n))
        if x < n - 1:
            heappush(candidate, (rot[x + 1][y] + c, i, i + n))
        if y:
            heappush(candidate, (rot[x][y - 1] + c, i, i - 1))
        if y < n - 1:
            heappush(candidate, (rot[x][y + 1] + c, i, i + 1))

for c, u, v in candidate:
    link(s - 1, u)
    link(u, v, 1, -c)
    link(v, t)

res = total
while 1:
    visit = [-1] * node
    is_inQ = [0] * node
    dist = [INF] * node

    SPFA = deque([s])
    is_inQ[s] = 1
    dist[s] = 0
    while SPFA:
        now = SPFA.popleft()
        is_inQ[now] = 0
        for next in capa[now]:
            if capa[now][next] - flow[now][next] > 0 and dist[next] > dist[now] + cost[now][next]:
                dist[next] = dist[now] + cost[now][next]
                visit[next] = now
                if is_inQ[next] == 0:
                    is_inQ[next] = 1
                    SPFA.append(next)

    if visit[t] == -1: break

    f, r = INF, t
    while r != s:
        f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
        r = visit[r]

    r = t
    while r != s:
        flow[visit[r]][r] += f
        flow[r][visit[r]] -= f
        res += cost[visit[r]][r]
        r = visit[r]

print(res)