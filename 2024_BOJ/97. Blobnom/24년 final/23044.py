# 23044: 트리 조각하기
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    eliminate = [0] + list(map(int, input().split()))
    step = [0] * (n + 1)
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    bfs = deque([])
    result = n
    for i in range(1, n + 1):
        if eliminate[i]:
            for j in tree[i]:
                if eliminate[j]:
                    continue
                else:
                    step[i] = 1
                    bfs.append(i)
                    break
    while bfs:
        now = bfs.popleft()
        explose = True
        for next in tree[now]:
            if eliminate[next] and step[next] == 0:
                step[next] = step[now] + 1
                bfs.append(next)
                explose = False
        if explose:
            result = min(result, step[now])
            break
    print(result)
solution()