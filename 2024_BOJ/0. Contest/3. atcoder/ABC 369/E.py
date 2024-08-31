import sys
from itertools import permutations
input = sys.stdin.readline
inf = int(1e15)
N,M = map(int,input().split())
graph = [[inf]*(N+1) for _ in range(N+1)]
bridg = [0]
for _ in range(M):
    a,b,t = map(int,input().split())
    if graph[a][b] > t:
        graph[a][b] = t
        graph[b][a] = t
    bridg.append((a,b,t))

for i in range(1,N+1):
    graph[i][i] = 0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(int(input())):
    K = int(input())
    B = list(map(int,input().split()))
    high = inf
    for row in permutations([i for i in range(K)],K):
        for bit in range(1<<K):
            res = 0
            order = [1]
            for k in range(K):
                a,b,t = bridg[B[row[k]]]
                if (1<<(K-1))>>k & bit:
                    res += graph[order[-1]][a]
                    order.append(b)
                else:
                    res += graph[order[-1]][b]
                    order.append(a)
                res += t
            res += graph[order[-1]][N]
            if high > res: high = res
    print(high)