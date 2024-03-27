#11403: 경로 찾기
import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
fw = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j]: fw[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if fw[i][k] and fw[k][j]: fw[i][j] = 1

for i in range(N):
    print(*fw[i])