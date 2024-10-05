#23887: 프린트 전달
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    N, M, K = map(int, input().split())
    stu = [[0] * (M + 1) for _ in range(N + 1)]
    cor = dict()
    for i in range(1, K + 1):
        X, Y = map(int, input().split())
        stu[X][Y] = i
        cor[i] = (X, Y)
    S = int(input())
    link = [0] * (K + 1)
    paper = [0] * (K + 1)
    link[S] = -1
    link[0] = -1
    bfs = deque([S])
    new = []
    while bfs:
        now = bfs.popleft()
        for i in range(8):
            dx, dy = cor[now]
            dx += d[i][0]
            dy += d[i][1]
            if 0 < dx <= N and 0 < dy <= M and link[stu[dx][dy]] == 0:
                new.append(stu[dx][dy])
                link[stu[dx][dy]] = now
        if not bfs:
            new.sort()
            bfs += new
            new.clear()
    for i in range(1, K + 1):
        k = i
        if link[k] == 0:
            print(-1)
            return
        while k >= 0:
            paper[k] += 1
            k = link[k]
    print(*paper[1:])
solution()