# 11498: 홀수 싸이클
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(now):
    global count
    count += 1
    visit[now] = 1
    num[now] = low[now] = count
    stack.append(now)

    for next in edge[now]:
        if num[next] == 0:
            dfs(next)
            low[now] = min(low[now], low[next])
        elif visit[next]:
            low[now] = min(low[now], num[next])

    if num[now] == low[now]:
        comp = []
        while stack:
            c = stack.pop()
            visit[c] = 0
            comp.append(comp)
            if c == now: break
        if len(comp) > 2:
            # scc 내 싸이클 확인
            # back edge만 coloring
            pass


for _ in range(int(input())):
    n, m = map(int, input().split())
    edge = [[] for _ in range(n + 1)]
    for __ in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)

    count = 0
    depth, visit, num, low = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    stack = []

    res, route = 0, []
    for i in range(1, n + 1):
        if num[i] == 0:
            dfs(i)