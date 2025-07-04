# 11406: 책 구매하기 2
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
node = n + m + 2
s, e = 0, n + m + 1
capa = [[0] * (node) for _ in range(node)]
flow = [[0] * (node) for _ in range(node)]
edge = [[] for _ in range(node)]
a = list(map(int, input().split()))
for i in range(1, n + 1):
    capa[s][i] = a[i - 1]
    edge[s].append(i)
    edge[i].append(s)
b = list(map(int, input().split()))
for i in range(n + 1, e):
    capa[i][e] = b[i - n - 1]
    edge[e].append(i)
    edge[i].append(e)
for j in range(n + 1, e):
    can_sell = list(map(int, input().split()))
    for i in range(1, n + 1):
        capa[i][j] = can_sell[i - 1]
        edge[i].append(j)
        edge[j].append(i)

res = 0

while 1:
    bfs = deque([s])
    visit = [-1] * (node)
    visit[s] = 0
    while bfs:
        now = bfs.popleft()
        for next in edge[now]:
            if capa[now][next] - flow[now][next] > 0 and visit[next] == -1:
                visit[next] = now
                bfs.append(next)
                if next == e:
                    bfs.clear()
                    break
    if visit[e] == -1: break

    f = float('inf')
    route = e
    while route != s:
        f = min(f, capa[visit[route]][route] - flow[visit[route]][route])
        route = visit[route]

    route = e
    while route != s:
        flow[visit[route]][route] += f
        flow[route][visit[route]] -= f
        route = visit[route]

    res += f
print(res)