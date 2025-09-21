# 22870: 산책 (large)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
link = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    link[a].append((b, c))
    link[b].append((a, c))
for i in range(1, n + 1):
    link[i].sort()
s, e = map(int, input().split())

def dijk(s, visited):
    dist = [INF] * (n + 1)
    dist[s] = 0
    hq = []
    heappush(hq, (0, s))

    while hq:
        d, now = heappop(hq)
        if dist[now] < d: continue

        for nxt, cost in link[now]:
            if nxt in visited: continue
            if dist[nxt] > d + cost:
                dist[nxt] = d + cost
                heappush(hq, (dist[nxt], nxt))

    return dist

dist = dijk(e, {})
depart_cost = 0
idx = s
visited = set()
while idx != e:
    for nxt, cost in link[idx]:
        if depart_cost + cost + dist[nxt] == dist[s]:
            depart_cost += cost
            idx = nxt
            visited.add(idx)
            break

visited.remove(e)
dist = dijk(s, visited)
print(depart_cost + dist[e])