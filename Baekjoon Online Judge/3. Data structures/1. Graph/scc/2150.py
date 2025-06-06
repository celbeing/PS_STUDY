# 2150: Strongly Connected Component
import sys
from collections import deque
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
v, e = map(int, input().split())
edge = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    edge[a].append(b)

visit = [0] * (v + 1)
num = [0] * (v + 1)
low = [i for i in range(v + 1)]
scc = []
cnt = 0
stack = deque()

def dfs(now):
    global cnt
    cnt += 1
    stack.append(now)
    visit[now] = 1
    num[now] = cnt
    low[now] = cnt

    for next in edge[now]:
        if num[next] == 0:
            dfs(next)
            low[now] = min(low[now], low[next])
        elif visit[next]:
            low[now] = min(low[now], num[next])

    if low[now] == num[now]:
        comp = []
        while stack:
            comp.append(stack.pop())
            visit[comp[-1]] = 0
            if now == comp[-1]: break
        comp.sort()
        scc.append(comp)

for i in range(1, v + 1):
    if num[i] == 0: dfs(i)
scc.sort()
print(len(scc))
for c in scc:
    print(*c + [-1])