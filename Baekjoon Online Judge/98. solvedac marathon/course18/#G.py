#23887: 프린트 전달
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    N, M, K = map(int, input().split())
    graph = dict()
    stu = dict()
    for i in range(1, K + 1):
        X, Y = map(int, input().split())
        graph[i] = []
        stu[(X, Y)] = i
        for de in d:
            dx = X + de[0]
            dy = Y + de[1]
            node = stu.get((dx, dy), 0)
            if node:
                graph[i].append(node)
                graph[node].append(i)
    S = int(input())
    bfs = deque([S])
    link = [0] * (K + 1)
    depth= [0] * (K + 1)
    link[S] = K + 1
    while bfs:
        new = []
        while bfs:
            now = bfs.popleft()
            for next in graph[now]:
                if now < link[next] and depth[next] == depth[now] + 1:


    paper = [0] * (K + 1)
    for i in range(1, K + 1):
        k = i
        while k:
            paper[k] += 1
            k = link[k]
    print(*paper[1:])
solution()