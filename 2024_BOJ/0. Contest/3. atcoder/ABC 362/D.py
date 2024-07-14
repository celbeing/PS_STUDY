import sys
from heapq import heappush, heappop
inf = int(1e15)
input = sys.stdin.readline

N,M = map(int,input().split())
A = [0]+list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
distance = [{} for _ in range(N+1)]
dist = [inf]*(N+1)

for _ in range(M):
    U,V,B = map(int,input().split())
    if V in graph[U]:
        if distance[U][V] > B:
            distance[U][V] = B
            distance[V][U] = B
    else:
        graph[U].append(V)
        graph[V].append(U)
        distance[U][V] = B
        distance[V][U] = B

h = []
heappush(h,(A[1],1))
while h:
    d,n = heappop(h)
    if d > dist[n]: continue
    for next in graph[n]:
        new_d = d+A[next]+distance[n][next]
        if dist[next] > new_d:
            dist[next] = new_d
            heappush(h,(new_d,next))
print(*dist[2:])