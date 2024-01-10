#9370: 미확인 도착지
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = 1e9
T=int(input())

def dijk(s):
    q = []
    distance = [inf]*(n+1)
    heappush(q,(0,s))
    distance[s] = 0

    while q:
        now, node = heappop(q)
        if distance[node] < now:
            continue
        for weight, next in graph[node]:
            new = now + weight
            if distance[next] > new:
                distance[next] = new
                heappush(q, (new, next))

    return distance


for t in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    destination = []

    for j in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    for j in range(t):
        destination.append(int(input()))

    s_dijk = dijk(s)
    g_dijk = dijk(g)
    h_dijk = dijk(h)

    result = []

    for d in destination:
        if s_dijk[g]+g_dijk[h]+h_dijk[d] == s_dijk[d] or s_dijk[h]+h_dijk[g]+g_dijk[d] == s_dijk[d]:
            result.append(d)

    result.sort()

    print(*result)