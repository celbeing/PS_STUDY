from collections import deque
n, m = map(int, input().split())
tree = [dict() for _ in range(n + 1)]
for _ in range(1, n):
    u, v, w = map(int, input().split())
    tree[u][v] = w
    tree[v][u] = w
for _ in range(m):
    a, b = map(int,input().split())
    check = [0] * (n + 1)
    check[a] = 1
    bfs = deque([(0, a)])
    while bfs:
        dist, now = bfs.popleft()
        if now == b:
            print(dist)
            break

        for next in tree[now]:
            if check[next]: continue
            check[next] = 1
            bfs.append((dist + tree[now][next], next))
    bfs.clear()