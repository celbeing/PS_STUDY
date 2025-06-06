# 30709: 외판원 순회 로봇
import sys
from collections import deque
input = sys.stdin.readline
inf = 10**9

def tsp(now, dstn, visit):
    if now == dstn:
        if visit + 1 == 1 << n:
            dp[now][dstn][visit] = 0
        else: return inf

    elif dp[now][dstn][visit] == inf:
        for next in range(1, n):
            if visit & (1 << next) or dist[now][next] == inf: continue
            dp[now][dstn][visit] = min(dp[now][dstn][visit], tsp(next, dstn, visit | (1 << next)) + dist[now][next])
    return dp[now][dstn][visit]

def fw_tsp(now, dstn, visit):

    for k in range(n):
        if visit & 1 << k: continue
        for b in bit_groups[visit]:
            q = visit | (1 << n) - ((1 << n) | b)

def scc_dfs(now, count):
    visited[now] = count
    stack.append(now)

    ret = visited[now]
    for next in range(1, n):
        if dist[now][next] == inf: continue

        if visited[next] == 0:
            ret = min(ret, scc_dfs(next, count + 1))
        elif finished[next] == 0:
            ret = min(ret, visited[next])

    if ret == visited[now]:
        comp = []
        while stack:
            t = stack.pop()
            comp.append(t)
            finished[t] = 1
            if t == now: break
        scc.append(sorted(comp))

    return ret

n, m, u, v = map(int, input().split())
n += 1
dist = [[inf] * n for _ in range(n)]
for _ in range(m):
    x, y, l = map(int, input().split())
    dist[x][y] = l
for k in range(1, n):
    dist[k][k] = 0
    for i in range(1, n):
        for j in range(1, n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# dp[i][j][v] = i에서 j로 v에 포함되지 않는 곳을 거쳐 가는 최단 거리
dp = [[[inf] * (1 << n) for _ in range(n)] for _ in range(n)]
ndp = [[[inf] * (1 << n) for _ in range(n)] for _ in range(n)]

visited = [0] * n
finished = [0] * n
scc = []
stack = deque()

# 방문 해야 할 비트의 부분집합 관리
bit_groups = [[] for _ in range(1 << n)]
for i in range(1 << n):
    for j in range(i + 1, 1 << n):
        if i & j == i:
            bit_groups[j].append(i)

# scc[-1]: 출발점 그룹
# scc[0]: 도착점 그룹
for i in range(1, n):
    if finished[i] == 0:
        scc_dfs(i, 1)

for i in scc[-1]:
    dist[0][i] = 0

for i in scc[0]:
    tsp(0, i, 1)

print()