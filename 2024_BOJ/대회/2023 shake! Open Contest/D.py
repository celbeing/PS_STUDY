#D: 모비스터디
import sys
from heapq import heappush, heappop
from collections import deque

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

distance = [inf for _ in range(N + 1)]
q = []
heappush(q, (0, A))
distance[A] = 0
while q:
    dist, now = heappop(q)
    if dist > distance[B]:
        break
    if dist > distance[now]:
        continue
    for next_node, next_dist in graph[now]:
        new_dist = dist+next_dist
        if distance[next_node] < new_dist:
            continue
        elif distance[next_node] == new_dist:
            before[next_node].append(now)
        else:
            heappush(q,(new_dist,next_node))
            distance[next_node] = new_dist
            before[next_node].clear()
            before[next_node].append(now)

result = []
dq = deque()
dq.append(B)
while dq:
    path = dq.popleft()
    if not(path in result):
        result.append(path)
    for a in before[path]:
        if not(a in result):
            dq.append(a)

result.sort()
print(len(result))
print(*result)