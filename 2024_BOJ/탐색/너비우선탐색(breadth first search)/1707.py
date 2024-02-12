#1707: 이분 그래프(graph)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, s):
    dq = deque()
    dq.append(s)
    if check[s] == 0:
        check[s] = 1

    while dq:
        v = dq.popleft()
        for u in graph[v]:
            if check[v] == check[u]:
                return False
            elif check[u] == 0:
                dq.append(u)
                check[u] = -check[v]
    return True

K = int(input())
for k in range(K):
    V,E = map(int,input().split())
    graph = dict()
    for v in range(1,V+1):
        graph[v] = []
    for e in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    check = [0 for v in range(V+1)]
    biparite = True
    for i in range(1,V+1):
        if not(bfs(graph,i)):
            biparite = False
            break
    if biparite:
        print("YES")
    else:
        print("NO")