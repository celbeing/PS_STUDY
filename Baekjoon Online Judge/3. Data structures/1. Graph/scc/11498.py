# 11498: 홀수 싸이클
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

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

def cycle(now):
    for next in edge[now]:
        if scc_num[next] != scc_num[now]: continue

        a = (now - 1) % n + 1
        b = (next - 1) % n + 1
        if check[a] == check[b]:
            route.append(b)
            return
        elif check[b] == 0:
            check[b] = 2 if check[a] == 1 else 1
            cycle(next)
            if route:
                if len(route) > 1 and route[0] == route[-1]: return
                route.append(b)
                return
            check[b] = 0

for _ in range(int(input())):
    n, m = map(int, input().split())
    edge = [[] for _ in range(n * 2 + 1)]
    for __ in range(m):
        u, v = map(int, input().split())
        edge[u].append(v + n)
        edge[u + n].append(v)

    count, scc_count = 0, 0
    visit, num, low = [0] * (n * 2 + 1), [0] * (n * 2 + 1), [0] * (n * 2 + 1)
    scc_num = [0] * (n * 2 + 1)
    stack = []

    res, route = 0, []
    for i in range(1, n * 2 + 1):
        if num[i] == 0:
            dfs(i)
    for i in range(1, n + 1):
        if scc_num[i] == scc_num[i + n]:
            check = [0] * (n + 1)
            route = []
            check[i] = 1
            cycle(i)
            if route[0] == route[-1]: route.pop()
            route.reverse()
            print(1)
            print(len(route))
            for r in route:
                print(r)
            break
    else:
        print(-1)