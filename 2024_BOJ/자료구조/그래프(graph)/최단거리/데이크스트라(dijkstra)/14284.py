#14284: 간선 이어가기 2
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
s,t = map(int,input().split())
distance = [int(1e9)] * (n + 1)

def dijk(graph,s,d):
    hq = []
    heappush(hq,(0,s))
    distance[s] = 0
    while hq:
        dist, node = heappop(hq)
        if node == d:
            return distance[d]
        if distance[node] < dist: continue
        for edge, next in graph[node]:
            new_dist = dist + edge
            if distance[next] > new_dist:
                distance[next] = new_dist
                heappush(hq,(new_dist,next))

print(dijk(graph,s,t))