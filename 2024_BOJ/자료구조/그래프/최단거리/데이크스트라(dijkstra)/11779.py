#11779: 최소비용 구하기 2
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = 1e9
n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
dist = [inf for _ in range(n+1)]
path = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int,input().split())
    bus[start].append((end, cost))
A, B = map(int,input().split())
path[A] = [A]
dist[A] = 0
dijk = []
heappush(dijk,(0,A))
while dijk:
    d, now = heappop(dijk)
    if now == B:
        break
    if dist[now] < d: continue
    for next, cost in bus[now]:
        new_d = d + cost
        if new_d < dist[next]:
            heappush(dijk,(new_d,next))
            dist[next] = new_d
            path[next] = path[now] + [next]
print(dist[B])
print(len(path[B]))
print(*path[B])