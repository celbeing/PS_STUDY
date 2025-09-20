# 22868: 산책 (small)
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
link = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
for i in range(1, n + 1):
    link[i].sort()
s, e = map(int, input().split())

dist = [-1] * (n + 1)
dist[s] = 0
goto = [i for i in range(n + 1)]
dq = deque([s])
while dq:
    now = dq.popleft()
    for nxt in link[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            dq.append(nxt)
            goto[nxt] = now
        if nxt == e:
            dq.clear()
            break

visited = set()
r = e
while goto[r] != s:
    visited.add(goto[r])
    r = goto[r]

dist = [-1] * (n + 1)
dist[e] = 0
dq.append(e)
while dq:
    now = dq.popleft()
    for nxt in link[now]:
        if nxt in visited or dist[nxt] > -1: continue
        dist[nxt] = dist[now] + 1
        dq.append(nxt)
        if nxt == s:
            print(dist[s] + len(visited) + 1)
            exit()