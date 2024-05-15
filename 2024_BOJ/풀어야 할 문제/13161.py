# 13161: 분단의 슬픔
import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)

N = int(input())
camp = list(map(int,input().split()))
capa = [[0]*(N+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+2)]
flow = [[0]*(N+2) for _ in range(N+2)]

for i in range(N):
    if camp[i] == 1:
        capa[0][i + 1] = inf
        capa[i + 1][0] = inf
    elif camp[i] == 2:
        capa[N + 1][i + 1] = inf
        capa[i + 1][N + 1] = inf

graph = [[] for _ in range(N+2)]
for i in range(N+2):
    for j in range(N+2):
        if capa[i][j] > 0: graph[i].append(j)

# 유량 보내주기
def make_flow(now,cut):
    if now == N+1: return cut
    for next in graph[now]:
        residual = capa[now][next]-flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            if residual > cut: residual = cut
            f = make_flow(next,residual)
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
    return 0

result = 0
while True:
    level = [-1] * (N + 2)
    level[0] = 0
    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if capa[now][next] - flow[now][next] > 0 and level[next] == -1:
                level[next] = level[now] + 1
                bfs.append(next)
    if level[-1] == -1: break

    stack = [(0, inf)]
    while stack:
        now, cut = stack[-1]
        for next in graph[now]:
            residual = capa[now][next] - flow[now][next]
            if level[now] + 1 == level[next] and residual > 0:
        else:

    # 최소 컷 탐색
    while True:
        f = make_flow(0,inf)
        if f == 0: break
        result += f

print(result)

visited = [False]*(N+2)
visited[0] = True
bfs = deque([0])
while bfs:
    now = bfs.popleft()
    for next in graph[now]:
        if not(visited[next]) and capa[now][next]-flow[now][next] > 0:
            visited[next] = True
            bfs.append(next)
A = []
B = []
for i in range(1,N+1):
    if visited[i]: A.append(i)
    else: B.append(i)
print(*A)
print(*B)