#D: 모비스터디
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = 1e15

N, M, A, B = map(int, input().split())
graph = [[] for _ in range(N + 1)]
before = dict()
for i in range(1, N + 1):
    before[i] = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(a):
    distance = [inf for _ in range(N+1)]
    distance[a] = 0
    q = []
    heappush(q, (0,a))
    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for next_node, next_dist in graph[now]:
            new_dist = dist + next_dist
            if distance[next_node] > new_dist:
                heappush(q, (new_dist, next_node))
                distance[next_node] = new_dist
                before[next_node].clear()
                before[next_node].append(now)
    return distance

a_dist = dijkstra(A)
b_dist = dijkstra(B)
short = a_dist[B]

result = []

for i in range(1, N+1):
    if a_dist[i]+b_dist[i] == short:
        result.append(i)

print(len(result))
print(*result)