#1967: 트리의 지름
import sys
from collections import deque
input = sys.stdin.readline
inf = 1e9

n = int(input())
tree = dict()
for i in range(1, n + 1):
    tree[i] = []
distance = [inf] * (n + 1)
for i in range(n - 1):
    edge = list(map(int,input().split()))
    tree[edge[0]].append((edge[1],edge[2]))
    tree[edge[1]].append((edge[0],edge[2]))

peek = 0
leaf = 0
bfs = deque()
bfs.append(1)
distance[1] = 0
while bfs:
    node = bfs.popleft()
    count = 0
    for next, dist in tree[node]:
        if distance[next] == inf:
            bfs.append(next)
            distance[next] = distance[node] + dist
            count += 1
    if count == 0 and distance[node] >= peek:
        peek = distance[node]
        leaf = node

peek = 0
bfs.append(leaf)
distance = [inf] * (n + 1)
distance[leaf] = 0
while bfs:
    node = bfs.popleft()
    count = 0
    for next, dist in tree[node]:
        if distance[next] == inf:
            bfs.append(next)
            distance[next] = distance[node] + dist
            count += 1
    if count == 0 and distance[node] >= peek:
        peek = distance[node]

print(peek)