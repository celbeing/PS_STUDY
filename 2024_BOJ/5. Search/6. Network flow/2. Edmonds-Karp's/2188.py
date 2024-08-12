# 2188: 축사 배정
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
capa = [[0]*(N+M+2) for _ in range(N+M+2)]
flow = [[0]*(N+M+2) for _ in range(N+M+2)]
result = 0
for i in range(1,N+1):
    link = list(map(int,input().split()))
    for j in range(1,link[0]+1):
        capa[i][link[j]+N] = 1

# source와 소는 모두 연결되어있다.
for i in range(1,N+1):
    capa[0][i] = 1

# 축사와 sink는 모두 연결되어있다.
for i in range(N+1,N+M+1):
    capa[i][N+M+1] = 1

while True:
    visit = [0]*(N+M+2)
    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        for next in range(0,N+M+2):
            if capa[now][next]-flow[now][next] > 0 and visit[next] == 0:
                visit[next] = now
                bfs.append(next)
                if next == N+M+1: break
    if visit[N+M+1] == 0: break
    route = N+M+1
    while route > 0:
        flow[visit[route]][route] += 1
        flow[route][visit[route]] -= 1
        route = visit[route]
    result += 1

print(result)