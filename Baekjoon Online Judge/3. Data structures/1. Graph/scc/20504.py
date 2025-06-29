# 20504: I번은 쉬운 문제
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dfs(now):
    global count, scc_count
    count += 1
    visit[now] = 1
    num[now] = count
    low[now] = count
    stack.append(now)

    for next in edge[now]:
        if num[next] == 0:
            dfs(next)
            low[now] = min(low[now], low[next])
        elif visit[next]:
            low[now] = min(low[now], num[next])

    if num[now] == low[now]:
        scc_count += 1
        while stack:
            c = stack.pop()
            visit[c] = 0
            scc_num[c] = scc_count
            if c == now: break

n, m = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)

count = 0
scc_count = 0
visit = [0] * (n + 1)
num = [0] * (n + 1)
low = [0] * (n + 1)
scc_num = [0] * (n + 1)
stack = []

for i in range(1, n + 1):
    if num[i] == 0: dfs(i)

scc_indeg = [0] * (scc_count + 1)
for now in range(1, n + 1):
    for next in edge[now]:
        if scc_num[now] != scc_num[next]:
            scc_indeg[scc_num[next]] += 1

need = 0
for i in range(1, scc_count + 1):
    if scc_indeg[i] == 0:
        need += 1

check = set()
for _ in range(int(input())):
    t = int(input())
    if scc_indeg[scc_num[t]] == 0:
        check.add(scc_num[t])

if len(check) == need:
    print(need)
else:
    print(-1)