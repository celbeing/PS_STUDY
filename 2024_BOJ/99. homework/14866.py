# 14866: 산만한 고양이
import sys
sys.setrecursionlimit(300001)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
sub_graph = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0] * (n + 1)
dfs_count = 1
n -= 1

def dfs(now):
    global dfs_count
    if now > 1: sub_graph[now] = 1
    check[now] = dfs_count
    near = dfs_count
    dfs_count += 1
    for next in graph[now]:
        if check[next] and near > check[next]:
            near = check[next]
        elif check[next] == 0:
            sub = dfs(next)
            if check[now] <= sub:
                sub_graph[now] += 1
            elif near > sub:
                near = sub
    return near

dfs(1)

res = 0
for i in range(1, n + 2):
    if m - len(graph[i]) == n - sub_graph[i]:
        res += i
print(res)