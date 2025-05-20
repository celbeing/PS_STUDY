# 2207: 가위바위보
import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(m * 2 + 1)]
    for _ in range(n):
        x, y = map(int, input().split())
        graph[-x].append(y)
        graph[-y].append(x)

    dfsn = [0] * (m * 2 + 1)
    finished = [0] * (m * 2 + 1)
    stack = deque()

    def dfs(now, cnt):
        dfsn[now] = cnt
        stack.append(now)

        res = dfsn[now]
        for next in graph[now]:
            if dfsn[next] == 0:
                res = min(res, dfs(next, cnt + 1))
            elif finished[next] == 0:
                res = min(res, dfsn[next])

        if res == dfsn[now]:
            scc = set()
            while stack:
                t = stack.pop()
                if -t in scc:
                    print('OTL')
                    exit()
                else:
                    scc.add(t)
                finished[t] = 1
                if t == now: break
        return res

    for i in range(-m, m + 1):
        dfs(i, 1)

    print('^_^')
solution()