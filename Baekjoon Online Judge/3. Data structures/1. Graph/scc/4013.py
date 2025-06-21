# 4013: ATM
import sys
sys.setrecursionlimit(500000)
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
        comp = []
        atm_total = 0
        is_restaurant = False
        while stack:
            c = stack.pop()
            atm_total += atm[c]
            if c in restaurant:
                is_restaurant = True
            visit[c] = 0
            scc_num[c] = scc_count
            comp.append(c)
            if c == now: break
        scc.append(comp)
        scc_atm.append(atm_total)
        scc_restaurant.append(1 if is_restaurant else 0)
    return 0

def scc_dfs(now):
    ret = scc_atm[now]
    flag = 1 if scc_restaurant[now] else 0
    high = 0
    for next in scc_edge[now]:
        g, f = scc_dfs(next)
        if f:
            flag = 1
            high = max(high, g)
    return (ret + high) if flag else 0, flag

n, m = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
atm = [0] + [int(input()) for _ in range(n)]
s, p = map(int, input().split())
restaurant = set(map(int, input().split()))

count, scc_count = 0, -1
visit, num, low, scc_num = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
stack, scc, scc_atm, scc_restaurant = [], [], [], []

for i in range(1, n + 1):
    if num[i] == 0: dfs(i)

scc_edge = [set() for _ in range(len(scc))]
for i in range(1, n + 1):
    now = scc_num[i]
    for j in edge[i]:
        next = scc_num[j]
        if now == next: continue
        scc_edge[now].add(next)

print(scc_dfs(scc_num[s])[0])

# translate by gpt
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
edge = [[] for _ in range(n + 1)]
rev_edge = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    rev_edge[v].append(u)

atm = [0] + [int(input()) for _ in range(n)]
s, p = map(int, input().split())
restaurant_nodes = set(map(int, input().split()))

visited = [False] * (n + 1)
order = []

for i in range(1, n + 1):
    if not visited[i]:
        stack = [(i, 0)]
        while stack:
            u, idx = stack.pop()
            if idx == 0:
                if visited[u]:
                    continue
                visited[u] = True
            if idx < len(edge[u]):
                stack.append((u, idx + 1))
                v = edge[u][idx]
                if not visited[v]:
                    stack.append((v, 0))
            else:
                order.append(u)

visited = [False] * (n + 1)
scc_num = [0] * (n + 1)
scc_count = 0

for u in reversed(order):
    if not visited[u]:
        scc_count += 1
        stack = [u]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            scc_num[v] = scc_count
            for w in rev_edge[v]:
                if not visited[w]:
                    stack.append(w)

scc_atm = [0] * (scc_count + 1)
scc_restaurant = [0] * (scc_count + 1)
for v in range(1, n + 1):
    cid = scc_num[v]
    scc_atm[cid] += atm[v]
    if v in restaurant_nodes:
        scc_restaurant[cid] = 1

scc_edge = [set() for _ in range(scc_count + 1)]
for u in range(1, n + 1):
    cu = scc_num[u]
    for v in edge[u]:
        cv = scc_num[v]
        if cu != cv:
            scc_edge[cu].add(cv)

indegree = [0] * (scc_count + 1)
for u in range(1, scc_count + 1):
    for v in scc_edge[u]:
        indegree[v] += 1

queue = deque(u for u in range(1, scc_count + 1) if indegree[u] == 0)
topo = []
while queue:
    u = queue.popleft()
    topo.append(u)
    for v in scc_edge[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)

dp_value = [0] * (scc_count + 1)
dp_flag  = [False] * (scc_count + 1)

for u in reversed(topo):
    flag = bool(scc_restaurant[u])
    best_child = 0
    for v in scc_edge[u]:
        if dp_flag[v]:
            flag = True
            if dp_value[v] > best_child:
                best_child = dp_value[v]
    dp_flag[u] = flag
    dp_value[u] = (scc_atm[u] + best_child) if flag else 0

print(dp_value[scc_num[s]])
'''