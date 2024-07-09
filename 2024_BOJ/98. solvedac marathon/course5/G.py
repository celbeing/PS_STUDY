import sys
from heapq import heappush, heappop
inf = int(1e10)
input = sys.stdin.readline
N = int(input())
A,B,C = map(int,input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [{} for _ in range(N+1)]
for _ in range(M):
    D,E,L = map(int,input().split())
    if D in graph[E]:
        if distance[E][D] > L:
            distance[E][D] = L
            distance[D][E] = L
    else:
        graph[E].append(D)
        graph[D].append(E)
        distance[E][D] = L
        distance[D][E] = L

def dijk(s):
    dist = [inf]*(N+1)
    dist[s] = 0
    h = []
    heappush(h,(0,s))
    while h:
        d,now = heappop(h)
        for next in graph[now]:
            new_d = d+distance[now][next]
            if dist[next] > new_d:
                heappush(h,(new_d,next))
                dist[next] = new_d
    return dist

result = 0
rec = -1
a = dijk(A)
b = dijk(B)
c = dijk(C)
for i in range(1,N+1):
    k = min(a[i],min(b[i],c[i]))
    if k > rec:
        rec = k
        result = i
print(result)