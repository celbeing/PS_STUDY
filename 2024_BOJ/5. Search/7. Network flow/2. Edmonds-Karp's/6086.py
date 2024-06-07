# 6086: 최대 유량
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
capa = [[0]*52 for _ in range(52)]
flow = [[0]*52 for _ in range(52)]
for _ in range(N):
    _in = list(input().split())
    a = ord(_in[0])-65
    b = ord(_in[1])-65
    if a > 25: a -= 6
    if b > 25: b -= 6
    f = int(_in[2])
    capa[a][b] += f
    capa[b][a] += f
result = 0
while True:
    bfs = deque([0])
    vist = [-1]*52
    while bfs:
        n = bfs.popleft()
        for i in range(52):
            if capa[n][i]-flow[n][i] > 0 and vist[i] == -1:
                bfs.append(i)
                vist[i] = n
                if i == 25: break
    if vist[25] == -1: break
    f = int(1e9)
    route = 25
    while route > 0:
        if f > capa[vist[route]][route]-flow[vist[route]][route]:
            f = capa[vist[route]][route]-flow[vist[route]][route]
        route = vist[route]
    route = 25
    while route > 0:
        flow[vist[route]][route] += f
        flow[route][vist[route]] -= f
        route = vist[route]
    result += f
print(result)