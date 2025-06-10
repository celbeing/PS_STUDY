# 2152: 여행 계획 세우기
import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, s, t = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)

scc = []
stack = []
count = 0
low = [0] * (n + 1)
num = [0] * (n + 1)
vst = [0] * (n + 1)

def dfs(now):
    global count
    count += 1
    stack.append(now)

    vst[now] = 1
    low[now] = count
    num[now] = count

    for next in edge[now]:
        if num[next] == 0:
            dfs(next)
            low[now] = min(low[now], low[next])
        elif vst[next]:
            low[now] = min(low[now], num[next])

    if low[now] == num[now]:
        comp = []
        while stack:
            comp.append(stack.pop())
            vst[comp[-1]] = 0
            if now == comp[-1]: break
        scc.append(comp)

for i in range(1, n + 1):
    if num[i] == 0: dfs(i)

scc_id = [-1] * (n + 1)
scc_edge = [[] for _ in range(len(scc))]
scc_size = [0] * len(scc)
dp = [0] * len(scc)

for i in range(len(scc)):
    comp = scc[-i - 1]
    scc_size[i] = len(comp)
    for c in comp:
        scc_id[c] = i

s, t = scc_id[s], scc_id[t]

while scc:
    comp = scc.pop()
    link = set()
    for c in comp:
        for nxt in edge[c]:
            if scc_id[nxt] in link or scc_id[nxt] == scc_id[c]: continue
            link.add(scc_id[nxt])
            scc_edge[scc_id[c]].append(scc_id[nxt])

bfs = deque([s])
dp[s] = scc_size[s]
while bfs:
    now = bfs.popleft()
    for next in scc_edge[now]:
        if dp[next] < dp[now] + scc_size[next]:
            dp[next] = dp[now] + scc_size[next]
            bfs.append(next)

print(dp[t])