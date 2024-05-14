import sys
input = sys.stdin.readline
inf = int(1e9)+1
N = int(input())
D = [list(map(int,input().split())) for _ in range(N)]
graph = [[inf]*N for _ in range(N)]
for i in range(N):
    near = inf
    node = i
    for j in range(N):
        if i == j: continue
        if D[i][j] < near:
            near = D[i][j]
            node = j
    if node == i:
        print(-1)
        exit()
    graph[i][node] = near
    if graph[node][i] < near:
        print(-1)
        exit()
    graph[node][i] = near
print("DONE")