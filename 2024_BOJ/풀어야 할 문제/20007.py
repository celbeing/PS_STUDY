#20007: 떡 돌리기
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N,M,X,Y = map(int,input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijk(graph, s):
    dist = [int(1e9)]*N
    dist[s] = 0
    h = [(0,s)]
    while h:
        d,n = heappop(h)
        if dist[n] < d: continue
        for next, edge in graph[n]:
            new_d = d+edge
            if dist[next] > new_d:
                dist[next] = new_d
                heappush(h,(new_d,next))
    return dist

dist = sorted(dijk(graph,Y))
count = 1
sum = 0
for k in dist:
    if k*2 > X:
        count = -1
        break
    sum += k
    if sum*2 > X:
        count += 1
        sum = k
print(count)