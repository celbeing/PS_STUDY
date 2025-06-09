# 11281: 2-SAT - 4
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
node = n * 2 + 1
edge = [[] for _ in range(node)]
for _ in range(m):
    i, j = map(int, input().split())
    edge[-i].append(j)
    edge[-j].append(i)

visit = [0] * node
low = [i for i in range(-n, n + 1)]
num = [0] * node
count = 0
stack = deque()
scc = deque()
scc_num = [0] * node

def dfs(now):
    global count
    count += 1
    stack.append(now)
    visit[now] = count
    low[now] = count
    num[now] = count

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
            scc_num[comp[-1]] = len(scc)
            if comp[-1] == now: break
        scc.append(comp)

for i in range(-n, n + 1):
    if i == 0: continue
    if num[i] == 0: dfs(i)

poss = True
res = [0] * n
for i in range(1, n + 1):
    if scc_num[i] == scc_num[-i]:
        poss = False
        break
    if scc_num[i] < scc_num[-i]:
        res[i - 1] = 1
if poss:
    print(1)
    print(*res)
else:
    print(0)