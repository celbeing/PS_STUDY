# 15568: 개구리 3
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
node = n * 2 + 1
frog = [(0, 0, 0, 0)]
for _ in range(n): frog.append(tuple(map(int, input().split())))
lotus = [(0, 0)]
edge = [[] for _ in range(node)]
leaf = [[] for _ in range(n + 1)]

def neg(k):
    return k + (-n if k > n else n)

def org(k):
    return k - (n if k > n else 0)

for i in range(1, n + 1):
    a, b = map(int, input().split())
    leaf[a].append(i)
    if a != b: leaf[b].append(neg(i))
    else: edge[neg(i)].append(i)
    lotus.append((a, b))

for i in range(1, n + 1):
    for j in range(len(leaf[i]) - 1):
        for k in range(j + 1, len(leaf[i])):
            a, b = leaf[i][j], leaf[i][k]
            edge[a].append(neg(b))
            edge[b].append(neg(a))

for _ in range(m):
    a, b, t = map(int, input().split())
    t -= 1
    for p in leaf[a]:
        for q in leaf[b]:
            if frog[org(p)][t] == frog[org(q)][t]: continue
            edge[p].append(neg(q))
            edge[q].append(neg(p))

stack = []
count, scc_count = 0, 0
visit, num, low, scc_num = [0] * node, [0] * node, [0] * node, [0] * node

def dfs(now):
    global count, scc_count
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
        scc_count += 1
        while stack:
            c = stack.pop()
            visit[c] = 0
            scc_num[c] = scc_count
            if c == now: break

for i in range(1, node):
    if num[i] == 0: dfs(i)

res = []
for i in range(1, n + 1):
    if scc_num[i] == scc_num[neg(i)]:
        print('NO')
        break
    res.append((lotus[i][1 if scc_num[i] > scc_num[neg(i)] else 0], i))
else:
    print('YES')
    res.sort()
    print(*[i for _, i in res])