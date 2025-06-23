# 19703: 실험
import sys
sys.setrecursionlimit(1200010)
input = sys.stdin.readline

def dfs(now):
    global count, scc_count
    count += 1
    visit[now] = 1
    num[now], low[now] = count, count
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
            if now == c: break

n, m, a, b = map(int, input().split())
edge = [[] for _ in range((n + a + 5) * 2)]
group = [[] for _ in range(m + 1)]
for _ in range(a):
    i, g = map(int, input().split())
    group[g].append(i)
node = n * 2
for i in range(1, m + 1):
    for j in range(len(group[i]) - 1):
        u = group[i][j]
        v = group[i][j + 1]
        edge[u].append(node + j * 2 + 1)
        edge[node + j * 2 + 1].append(node + j * 2 + 3)
        edge[node + j * 2 + 1].append(v + n)
        edge[node + j * 2 + 2].append(u + n)
        edge[node + j * 2 + 4].append(node + j * 2 + 2)
        edge[v].append(node + j * 2 + 2)
    node += len(group[i]) * 2

for _ in range(b):
    i, j = map(int, input().split())
    edge[i + n].append(j)
    edge[j + n].append(i)

visit = [0] * ((n + a + 5) * 2)
num = [0] * ((n + a + 5) * 2)
low = [0] * ((n + a + 5) * 2)
scc_num = [0] * ((n + a + 5) * 2)
count, scc_count = 0, 0
stack = []

for i in range(1, n * 2 + 1):
    if num[i] == 0: dfs(i)


for i in range(1, n + 1):
    if scc_num[i] == scc_num[i + n]:
        print('NIE')
        break
else:
    print('TAK')