#1956: 운동
import sys
input = sys.stdin.readline
inf = 1e9

V,E = map(int,input().split())
dist = [[inf for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    dist[a][b] = c

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

result = inf
for i in range(1,V+1):
    if result > dist[i][i]:
        result = dist[i][i]

if result == inf:
    print(-1)
else:
    print(result)