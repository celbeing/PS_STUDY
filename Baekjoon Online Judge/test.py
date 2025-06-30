def dfs(now):
    global count
    count += 1
    stack.append(now)
    num[now] = count
    low[now] = count
    visit[now] = 1

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
            comp.append(c)
            if c == now: break
        scc.append(comp)

n, e = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(e):
    u, v = map(int, input().split())
    edge[u].append(v)

visit = [0] * (n + 1)
num = [0] * (n + 1)
low = [0] * (n + 1)
stack = []
scc = []
count = 0

for i in range(1, n + 1):
    if num[i] == 0: dfs(i)
