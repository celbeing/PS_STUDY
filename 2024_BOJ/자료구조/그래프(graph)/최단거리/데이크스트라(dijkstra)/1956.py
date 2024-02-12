#1956: 운동(메모리초과)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = 1e9

V,E = map(int,input().split())
road = [[] for _ in range(V+1)]
dist = [[inf for _ in range(V+1)] for _ in range(V+1)]
heap = []

for _ in range(E):
    a,b,c = map(int,input().split())
    road[a].append([c,b])
    dist[a][b] = c
    heappush(heap,[c,a,b])

while heap:
    d, s, e = heappop(heap)

    if s == e:
        print(d)
        break

    if dist[s][e] < d:
        continue

    for nowd, nexte in road[e]:
        nextd = d+nowd
        if nextd < dist[s][nexte]:
            dist[s][nexte] = nextd
            heappush(heap,[nextd,s,nexte])
else:
    print(-1)