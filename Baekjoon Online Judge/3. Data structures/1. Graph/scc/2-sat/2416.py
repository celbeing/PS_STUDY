# 2416: 문
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
node = m * 2 + 1
scc = []
visit = [0] * node
low = [i for i in range(-m, m + 1)]
num = [0] * node
stack = []
count = 0

edge = [[] for _ in range(node)]
for _ in range(n):
    a, sa, b, sb = map(int, input().split())
    if sa: a *= -1
    if sb: b *= -1
    edge[-a].append(b)
    edge[-b].append(a)

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
            if now == comp[-1]: break
        scc.append(comp)

for i in range(-m, m + 1):
    if i == 0: continue
    if num[i] == 0: dfs(i)

poss = True
res = [0] * (m + 1)
while scc:
    for c in scc[-1]:
        b = 1 if c > 0 else -1
        if res[c * b]