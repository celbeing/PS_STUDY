# 3977: 축구 전술
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(now):
    global count, scc_count
    count += 1
    stack.append(now)
    visit[now] = 1
    low[now] = num[now] = count

    for next in edge[now]:
        if num[next] == 0:
            dfs(next)
            low[now] = min(low[now], low[next])
        elif visit[next]:
            low[now] = min(low[now], num[next])

    if num[now] == low[now]:
        scc_count += 1
        comp = []
        while stack:
            c = stack.pop()
            visit[c] = 0
            scc_num[c] = scc_count
            comp.append(c)
            if now == c: break
        comp.sort()
        scc.append(comp)

for _ in range(int(input())):
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]

    count, scc_count = 0, 0
    visit, scc_num, num, low = [0] * n, [0] * n, [0] * n, [0] * n
    scc, stack = [], []

    for _ in range(m):
        a, b = map(int, input().split())
        edge[a].append(b)

    for i in range(n):
        if num[i] == 0: dfs(i)

    get_in = [0] * len(scc)
    for now in range(n):
        for next in edge[now]:
            if scc_num[now] == scc_num[next]: continue
            get_in[scc_num[next] - 1] += 1

    dt = -1
    for i in range(scc_count):
        if get_in[i]: continue
        elif dt >= 0:
            print('Confused')
            break
        else: dt = i
    else:
        for c in scc[dt]:
            print(c)
    input()
    print()