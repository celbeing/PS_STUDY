# 32182: POEM
import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
node = n * 2 + 2
edge_min = [[] for _ in range(node)]
edge_odd = [[] for _ in range(node)]
n_state = [i for i in range(0, n * 2 + 1, 2)]

minus = [-1] * (n + 1)
odd = [-1] * (n + 1)

for _ in range(m):
    q, l, r = input().split()
    l, r = int(l) - 1, int(r)
    if q == 'P':
        edge_min[l].append(r)
        edge_min[r].append(l)
        edge_min[l + n + 1].append(r + n + 1)
        edge_min[r + n + 1].append(l + n + 1)
    elif q == 'M':
        edge_min[l].append(r + n + 1)
        edge_min[r].append(l + n + 1)
        edge_min[l + n + 1].append(r)
        edge_min[r + n + 1].append(l)
    elif q == 'E':
        edge_odd[l].append(r)
        edge_odd[r].append(l)
        edge_odd[l + n + 1].append(r + n + 1)
        edge_odd[r + n + 1].append(l + n + 1)
    else:
        edge_odd[l].append(r + n + 1)
        edge_odd[r].append(l + n + 1)
        edge_odd[l + n + 1].append(r)
        edge_odd[r + n + 1].append(l)

visit = [0] * node
scc_num = [0] * node
num = [0] * node
low = [0] * node
stack = []
count = 0
scc_count = 0

def dfs_odd(now):
    global count, scc_count
    count += 1
    visit[now] = 1
    num[now] = count
    low[now] = count
    stack.append(now)

    for next in edge_odd[now]:
        if num[next] == 0:
            dfs_odd(next)
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

def dfs_min(now):
    global count, scc_count
    count += 1
    visit[now] = 1
    num[now] = count
    low[now] = count
    stack.append(now)

    for next in edge_min[now]:
        if num[next] == 0:
            dfs_min(next)
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

for i in range(node):
    if num[i] == 0: dfs_odd(i)

for i in range(n + 1):
    if scc_num[i] == scc_num[i + n + 1]:
        print(0)
        exit()
    scc_num[i] = 1 if scc_num[i] < scc_num[i + n + 1] else 0

for i in range(1, n + 1):
    n_state[i] -= 1 if scc_num[i] ^ scc_num[i - 1] else 0

visit = [0] * node
scc_num = [0] * node
num = [0] * node
low = [0] * node
stack = []
count = 0
scc_count = 0

for i in range(node):
    if num[i] == 0: dfs_min(i)

for i in range(n + 1):
    if scc_num[i] == scc_num[i + n + 1]:
        print(0)
        exit()
    scc_num[i] = 1 if scc_num[i] < scc_num[i + n + 1] else 0

for i in range(1, n + 1):
    n_state[i] *= -1 if scc_num[i] ^ scc_num[i - 1] else 1

print(*n_state[1:])