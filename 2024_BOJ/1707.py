#1707: 이분 그래프
import sys
from collections import deque
input = sys.stdin.readline
bfs = deque()
K = int(input())
for k in range(K):
    V,E = map(int,input().split())
    graph = dict()
    for v in range(V):
        graph[v] = []
    for e in range(E):
        u,v = map(int,input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    check = [0 for v in range(V)]
    bfs.append(0)
    check[0] = 1
    biparite = True
    while bfs and biparite:
        v = bfs.popleft()
        for u in graph[v]:
            if check[v] == check[u]:
                biparite = False
                bfs.clear()
                break
            elif check[u] == 0:
                bfs.append(u)
                check[u] = -check[v]
        if not(bfs):
            for i in range(V):
                if check[i] == 0:
                    bfs.append(i)
                    check[i] = 1
    if biparite:
        print("YES")
    else:
        print("NO")