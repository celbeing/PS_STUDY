# 11281: 2-SAT - 4
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n * 2 + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[-i].append(j)
    graph[-j].append(i)

visit = [0] * (n * 2 + 1)
finished = [0] * (n * 2 + 1)
stack = deque()
scc = [[]]

def dfs(now, count):
    visit[now] = count
    stack.append(now)

    ret = visit[now]
    for next in graph[now]:
        if visit[next] == 0:
            ret = min(ret, dfs(next, count + 1))
        elif finished[next] == 0:
            ret = min(ret, visit[next])

    if ret == visit[now]:
        comp = []
        while stack:
            t = stack.pop()
            comp.append(t)
            finished[t] = len(scc)
            if t == now: break
        scc.append(sorted(comp))

    return ret

for i in range(-n, n + 1):
    if i == 0: continue
    if finished[i] == 0:
        dfs(i, 1)

scc_graph = [[] for _ in range(len(scc))]
in_degree = [0] * len(scc)
for now in range(-n, n + 1):
    if now == 0: continue
    for next in graph[now]:
        if finished[now] != finished[next]:
            scc_graph[finished[now]].append(finished[next])
            in_degree[finished[next]] += 1