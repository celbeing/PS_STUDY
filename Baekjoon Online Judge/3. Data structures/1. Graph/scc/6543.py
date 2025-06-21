# 6543: 그래프의 싱크
import sys
input = sys.stdin.readline

def dfs(now):
    global count, scc_count
    count += 1
    stack.append(now)
    visit[now] = 1
    num[now], low[now] = count, count

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
            if c == now: break
        comp.sort()
        scc.append(comp)

while True:
    q = input().strip()
    if q == '0': break

    n, m = map(int, q.split())
    uv = list(map(int, input().split()))
    edge = [[] for _ in range(n + 1)]
    for i in range(0, m * 2, 2):
        edge[uv[i]].append(uv[i + 1])

    count, scc_count = 0, 0
    visit, low, num, scc_num = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    stack, scc = [], []

    for i in range(1, n + 1):
        if num[i] == 0: dfs(i)

    sink = []
    while scc:
        comp = scc.pop()
        is_sink = True
        for now in comp:
            for next in edge[now]:
                if scc_num[now] != scc_num[next]:
                    is_sink = False
                    break
            if not is_sink: break
        if is_sink:
            sink += comp
    sink.sort()
    print(*sink)