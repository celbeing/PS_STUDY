# 15675: 괴도 강산
import sys
sys.setrecursionlimit(4000)
input = sys.stdin.readline

n, m = map(int, input().split())
node = (n + m) * 2 + 1
visit = [0] * node
num = [0] * node
low = [0] * node
count = 0
scc_count = 0
scc_num = [0] * node
stack = []

edge = [[] for _ in range(node)]

for i in range(n):
    line = list(input().strip())
    for j in range(m):
        if line[j] == '#':
            x, y = i + 1, j + n + 1
            edge[x].append(y)
            edge[y].append(x)
            edge[-x].append(-y)
            edge[-y].append(-x)
        elif line[j] == '*':
            x, y = i + 1, j + n + 1
            edge[x].append(-y)
            edge[-x].append(y)
            edge[y].append(-x)
            edge[-y].append(x)

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
            if now == c: break

for i in range(-n - m - 1, n + m + 1):
    if i == 0: continue
    if num[i] == 0: dfs(i)

res = [0] * (n + m + 1)
for i in range(1, n + m + 1):
    if scc_num[i] == scc_num[-i]:
        print(0)
        break
    if scc_num[i] < scc_num[-1]:
        res[i] = 1
else:
    print(1)