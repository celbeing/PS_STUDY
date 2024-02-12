#1238: 파티
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
inf = 1e9
N,M,X = map(int,input().split())
go = dict()
back = dict()
for i in range(1,N+1):
    go[i] = []
    back[i] = []
for _ in range(M):
    a,b,t = map(int,input().split())
    go[b].append((t,a))
    back[a].append((t,b))
distance_go = [inf] * (N+1)
distance_back = [inf] * (N+1)

distance_go[X] = 0
q = []
heappush(q,(0,X))
while q:
    dist, now = heappop(q)
    if distance_go[now] < dist: continue
    for node, next in go[now]:
        new_dist = dist + node
        if distance_go[next] > new_dist:
            heappush(q,(new_dist,next))
            distance_go[next] = new_dist

distance_back[X] = 0
q = []
heappush(q,(0,X))
while q:
    dist, now = heappop(q)
    if distance_back[now] < dist: continue
    for node, next in back[now]:
        new_dist = dist + node
        if distance_back[next] > new_dist:
            heappush(q,(new_dist,next))
            distance_back[next] = new_dist

result = 0
for i in range(1,N+1):
    t = distance_go[i] + distance_back[i]
    if t > result:
        result = t
print(result)