#32495: WALK
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    road = [dict() for _ in range(N + 1)]
    dist = [0] * (N + 1)
    time = [0] * (N + 1)
    for _ in range(M):
        a, b, c = map(int, input().split())
        road[a][b] = c
        road[b][a] = c
    bfs = [(0, 1, 0)]
    while bfs:
        t, now, d = heappop(bfs)
        for next in road[now]:
            if road[now][next] > t and dist[next] <= d:
                heappush(bfs, (road[now][next], next, d + 1))
                time[next] = road[now][next]
                dist[next] = d + 1
    print(*dist[1:])
solution()
