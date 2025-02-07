import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def solution():
    n, m = 299999, 300000
    graph = [[] for _ in range(n + 1)]
    edge = [0] * (n + 1)
    for i in range(1, 299996):
        a, b = i, i + 1
        graph[a].append(b)
        graph[b].append(a)
        edge[a] += 1
        edge[b] += 1
    graph[1].append(299997)
    graph[299997].append(1)
    graph[1].append(299998)
    graph[299998].append(299999)
    graph[299999].append(1)
    graph[299999].append(299998)
    graph[1].append(299999)
    graph[299998].append(1)
    edge[1] += 3
    edge[299997] += 1
    edge[299998] += 2
    edge[299999] += 2

    check = [0] * (n + 1)
    dfs_count = 1
    non_artic = set()
    n -= 2

    def dfs(now):
        nonlocal dfs_count
        check[now] = dfs_count
        near = dfs_count
        dfs_count += 1
        root_count = 0
        is_non_artic = True
        for next in graph[now]:
            if check[next] and near > check[next]:
                near = check[next]
            elif check[next] == 0:
                if now == 1: root_count += 1
                sub = dfs(next)
                if check[now] <= sub:
                    is_non_artic = False
                elif near > sub:
                    near = sub
        if is_non_artic:
            non_artic.add(now)
        if now == 1:
            return root_count
        else:
            return near

    if dfs(1) == 1:
        non_artic.add(1)

    res = 0
    for k in non_artic:
        if m - edge[k] <= n:
            res += k
    print(res)
solution()