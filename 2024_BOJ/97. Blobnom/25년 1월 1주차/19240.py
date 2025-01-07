# 19240: 장난감 동맹군
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    enemy = [[] for _ in range(n + 1)]
    group = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        enemy[x].append(y)
        enemy[y].append(x)
    bfs = deque([])
    for i in range(1, n + 1):
        if group[i]: continue
        bfs.append(i)
        group[i] = 1
        while bfs:
            now = bfs.popleft()
            for next in enemy[now]:
                if group[next] == group[now]:
                    print("NO")
                    return
                else:
                    if group[next] == 0: bfs.append(next)
                    group[next] = 1 if group[now] == 2 else 2
    print("YES")
for _ in range(int(input())):
    solution()