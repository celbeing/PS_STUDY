#1167: 트리의 지름
import sys
from collections import deque
input = sys.stdin.readline
inf = 1e9

V = int(input())
tree = dict()
distance = [inf] * (V+1)
for i in range(V):
    edge = list(map(int,input().split()))
    tree[edge[0]] = []
    for j in range(1,len(edge)-1,2):
        tree[edge[0]].append((edge[j],edge[j+1]))

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
distance = [inf] * (V+1)
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