#5213: 과외맨
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N = int(input())
    NN = N * 2 - 1
    link = [[] for _ in range(N * N - N // 2 + 1)]
    visit = [0] * (N * N - N // 2 + 1)
    tile = [(0,0)]
    for k in range(1, N * N - N // 2 + 1):
        tile.append(tuple(map(int, input().split())))
        if not(k % NN == 1 or k % NN == N + 1):
            if tile[k - 1][1] == tile[k][0]:
                link[k - 1].append(k)
                link[k].append(k - 1)
        if k > N:
            if k % NN != 1:
                if tile[k - N][1] == tile[k][0]:
                    link[k - N].append(k)
                    link[k].append(k - N)
            if k % NN != N:
                if tile[k - N + 1][0] == tile[k][1]:
                    link[k - N + 1].append(k)
                    link[k].append(k - N + 1)
    bfs = deque([1])
    visit[1] = -1
    while bfs:
        now = bfs.popleft()
        for next in link[now]:
            if visit[next]: continue
            bfs.append(next)
            visit[next] = now
    visit[1] = -1
    route = []
    k = N * N - N // 2
    while visit[k] == 0:
        k -= 1
    while k > 0:
        route.append(k)
        k = visit[k]
    route.reverse()
    print(len(route))
    print(*route)
solution()