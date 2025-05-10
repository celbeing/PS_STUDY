# 최소비용 구하기
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = int(1e9)
def solution():
    n = int(input())
    m = int(input())
    bus = [dict() for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        if v in bus[u]: bus[u][v] = min(bus[u][v], w)
        else: bus[u][v] = w
    dist = [inf] * (n + 1)
    s, e = map(int, input().split())
    dist[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        d, now = heappop(q)
        if now == e: break
        for next in bus[now]:
            new_d = d + bus[now][next]
            if dist[next] > new_d:
                dist[next] = new_d
                heappush(q, (new_d, next))
    print(dist[e])
solution()