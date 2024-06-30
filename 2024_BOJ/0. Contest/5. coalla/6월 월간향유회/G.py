import sys
input = sys.stdin.readline
inf = int(1e9)
n,m = map(int,input().split())
graph = [[[inf,i] for i in range(n)] for _ in range(n)]
node =[[i for i in range(1,n+1)] for j in range(1,n+1)]
for _ in range(m):
    u,v,t = map(int,input().split())
    u-=1;v-=1
    if graph[u][v][0] > t: graph[u][v] = [t,v]
    if graph[v][u][0] > t: graph[v][u] = [t,u]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if graph[i][j][0] > graph[i][k][0]+graph[k][j][0]:
                graph[i][j] = [graph[i][k][0] + graph[k][j][0],graph[i][k][1]]

for i in range(n):
    result = []
    for j in range(n):
        if i == j:
            result.append('-')
        else:
            result.append(str(graph[i][j][1]+1))
    print(*result)