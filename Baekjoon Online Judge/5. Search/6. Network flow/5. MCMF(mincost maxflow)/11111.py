# 11111: 두부장수 장홍준 2
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
score = {'A':0, 'B':1, 'C':2, 'D':3, 'F':4}

n, m = map(int, input().split())
plate = [list(input().strip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        plate[i][j] = score[plate[i][j]]
node = n * m + 2
s, t = 0, node - 1
grade = [[10, 8, 7, 5, 1], [8, 6, 4, 3, 1], [7, 4, 3, 2, 1], [5, 3, 2, 2, 1], [1, 1, 1, 1, 0]]

capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]
cost = [dict() for _ in range(node)]

def link(u, v, f = 1, c = 0):
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0
    cost[u][v] = -c
    cost[v][u] = c

for i in range(1, n * m + 1):
    link(s, i)
    link(i, t)
    x, y = (i - 1) // m, (i - 1) % m
    if (x + y) % 2 == 0:
        if x:
            c = grade[plate[x][y]][plate[x - 1][y]]
            link(i, i - m, 1, c)
        if x < n - 1:
            c = grade[plate[x][y]][plate[x + 1][y]]
            link(i, i + m, 1, c)
        if y:
            c = grade[plate[x][y]][plate[x][y - 1]]
            link(i, i - 1, 1, c)
        if y < m - 1:
            c = grade[plate[x][y]][plate[x][y + 1]]
            link(i, i + 1, 1, c)

high = 0
result = 0
while 1:
    visit = [-1] * node
    is_inQ = [0] * node
    dist = [INF] * node

    spfa = deque([0])
    visit[0] = 0
    is_inQ[0] = 1
    dist[0] = 0
    while spfa:
        now = spfa.popleft()
        is_inQ[now] = 0
        for next in capa[now]:
            if capa[now][next] - flow[now][next] > 0 and dist[next] > dist[now] + cost[now][next]:
                visit[next] = now
                dist[next] = dist[now] + cost[now][next]
                if is_inQ[next] == 0:
                    is_inQ[next] = 1
                    spfa.append(next)

    if visit[t] == -1: break

    f = INF
    r = t
    while r:
        f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
        r = visit[r]

    r = t
    sum = 0
    while r:
        flow[visit[r]][r] += f
        flow[r][visit[r]] -= f
        sum -= cost[visit[r]][r]
        r = visit[r]
    if sum < 0: break
    result += sum

print(result)