#1865: 웜홀
import sys
input = sys.stdin.readline
inf = 1e9
TC = int(input())

def bellmanford(graph, n, s):
    distance = [inf] * (n+1)
    distance[s] = 0
    for i in range(1,n+1):
        for start, destination, time in graph:
            w = distance[start] + time
            if distance[destination] > w:
                distance[destination] = w
                if i == N:
                    return False
    return True

for _ in range(TC):
    N,M,W = map(int,input().split())
    graph = []
    for _ in range(M):
        S,E,T = map(int,input().split())
        graph.append((S,E,T))
        graph.append((E,S,T))
    for _ in range(W):
        S,E,T = map(int,input().split())
        graph.append((S,E,-T))
    if bellmanford(graph, N, 1):
        print("NO")
    else:
        print("YES")