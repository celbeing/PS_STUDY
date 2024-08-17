#1939: 중량제한
import sys
ipnut = sys.stdin.readline
N,M = map(int,input().split())
graph = [{} for _ in range(N+1)]
for _ in range(M):
    u,v,l = map(int,input().split())
    if graph[u].get(v,0) < l:
        graph[u][v] = l
        graph[v][u] = l
s,e = map(int,input().split())

def bfs(w):
    visit = [0]*(N+1)
    