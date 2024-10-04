#23887: 프린트 전달
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    N, M, K = map(int, input().split())
    stu = dict()
    cor = dict()
    for i in range(1, K + 1):
        X, Y = map(int, input().split())
        stu[X * 1000 + Y] = i
        cor[i] = (X, Y)
    S = int(input())
    link = [-1] * (K + 1)
    paper = [0] * (K + 1)
    link[S] = 0
    bfs = deque([S])
    new = []
    while bfs:
        now = bfs.popleft()
        x, y = cor[now]
        for de in d:
            dx = x + de[0]
            dy = y + de[1]
            next = dx * 1000 + dy
            if next in stu and link[stu[next]] == -1:
                new.append(stu[next])
                link[stu[next]] = now
        if not bfs:
            new.sort(reverse=True)
            while new: bfs.append(new.pop())
    for i in range(1, K + 1):
        k = i
        if link[k] == -1:
            print(-1)
            return
        while k > 0:
            paper[k] += 1
            k = link[k]
    print(*paper[1:])
solution()
#재귀로 상향 탐색해야 될 것 같음