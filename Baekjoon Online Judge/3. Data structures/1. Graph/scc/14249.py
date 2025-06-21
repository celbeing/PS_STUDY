# 14249: 점프 점프 2
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
s = int(input())

def dfs(now):
    global count, scc_count
    count += 1
    visit[now] = 1
    num[now], low[now] = count, count
    stack.append(now)

    for next in (now - a[now], now + a[now]):
        if next < 1 or next > n: continue
        if num[next] == 0:
            dfs(next)
            low[now] = min(low[now], low[next])
        elif visit[next]:
            low[now] = min(low[now], num[next])

    if num[now] == low[now]:
        scc_count += 1
        scc_size.append(0)
        while stack:
            c = stack.pop()
            visit[c] = 0
            scc_num[c] = scc_count
            scc_size[-1] += 1
            if c == now: break

def scc_dfs(now):
    ret = scc_size[now]
    get = 0
    for next in scc_edge[now]:
        get = max(get, scc_dfs(next))
    return ret + get

count, scc_count = 0, -1
visit, num, low, scc_num = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
stack, scc_size = [], []

for i in range(1, n + 1):
    if num[i] == 0: dfs(i)

scc_edge = [set() for _ in range(len(scc_size))]

for now in range(1, n + 1):
    for next in (now - a[now], now + a[now]):
        if next < 1 or next > n or scc_num[now] == scc_num[next]: continue
        scc_edge[scc_num[now]].add(scc_num[next])

print(scc_dfs(scc_num[s]))