# 11097: 도시 계획
import sys
input = sys.stdin.readline

def dfs(now):
    global count
    count += 1
    k = count
    scc_num[k] = now
    check[now] = k
    step = now
    for next in range(n):
        if now == next: continue

        if region[now][next] == region[next][now] == 1:
            edge.append((step, next))
            check[next] = k
            step = next
        elif region[now][next] == 1:
            if check[next] == -1: dfs(next)
            edge.append((now, scc_num[check[next]]))
    if now != step:
        edge.append((step, now))

for _ in range(int(input())):
    input()
    n = int(input())
    edge = []
    count = -1
    check = [-1] * n
    scc_num = [-1] * n
    region = [list(map(int, list(input().strip()))) for _ in range(n)]
    for k in range(n):
        for i in range(n):
            if i == k: continue
            for j in range(n):
                if j == k: continue
                if region[i][k] and region[k][j] and region[i][j]:
                    region[i][j] = 0
    for i in range(n):
        if check[i] == -1:
            dfs(i)

    print(len(edge))
    for a, b in edge:
        print(a + 1, b + 1)
    print()