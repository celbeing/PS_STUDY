# 28120: SCCC 신입 부원 모집하기
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f = 1):
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0

n, k, x = map(int, input().split())
node = n + k + 2
capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]
study = [0] * (n + 1)
for i in range(1, n + 1): link(0, i)
for i in range(n + 1, node): link(i, node - 1, x)
for i in range(1, n + 1):
    for j in list(map(int, input().split()))[1:]:
        link(i, n + j)

s, e = 0, node - 1
while 1:
    bfs = deque([0])
    visit = [-1] * node

    while bfs:
        now = bfs.popleft()
        for next in capa[now]:
            if capa[now][next] - flow[now][next] > 0 and visit[next] == -1:
                visit[next] = now
                bfs.append(next)
                if next == e:
                    bfs.clear()
                    break

    if visit[e] == -1: break

    f = capa[visit[e]][e] - flow[visit[e]][e]
    r = visit[e]
    toggle = 1
    while r:
        f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
        if toggle:
            study[visit[r]] = r - n
            toggle = 0
        else:
            toggle = 1
        r = visit[r]

    r = e
    while r:
        flow[visit[r]][r] += f
        flow[r][visit[r]] -= f
        r = visit[r]
for i in range(1, k + 1):
    member = []
    for j in range(1, n + 1):
        if study[j] == i: member.append(j)
    print(len(member), *member)