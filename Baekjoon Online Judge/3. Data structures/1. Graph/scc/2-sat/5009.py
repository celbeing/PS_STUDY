# 5009: 유치원
import sys
input = sys.stdin.readline

n = int(input())
d = [(n, n * 2), (-n, n), (-(n * 2), -n)]
rank_dict = [dict() for _ in range(n + 1)]
rank = [[]]
cls = [0] * (n + 1)
for i in range(1, n + 1):
    rank.append(list(map(int, input().split())))
    cls[i] = rank[-1][0]
    for j in range(1, n):
        rank_dict[i][rank[-1][j]] = j

def get_rank(a, b, k):
    return 0 if rank_dict[a][b] <= k and rank_dict[b][a] <= k else 1

def sat(t):
    count, scc_count = 0, 0
    visit, num, low, scc_num = [0] * (n * 3 + 1), [0] * (n * 3 + 1), [0] * (n * 3 + 1), [0] * (n * 3 + 1)
    stack = []
    edge = [[] for _ in range(n * 2 + 1)]
    for a in range(1, n + 1):
        for b in rank[a][t + 1:]:
            if cls[a] == 0:
                if cls[b] == 0:
                    edge[a].append(b + n)
                    edge[b].append(a + n)
                    edge[a + n].append(b)
                    edge[b + n].append(a)
                elif cls[b] == 1:
                    edge[a + n].append(b)
                    edge[b + n].append(a)
                else:
                    edge[a].append(b)
                    edge[b + n].append(a + n)
            elif cls[a] == 1:
                if cls[b] == 0:
                    edge[a + n].append(b)
                    edge[b + n].append(a)
                elif cls[b] == 1:
                    edge[a].append(b + n)
                    edge[b].append(a + n)
                    edge[a + n].append(b)
                    edge[b + n].append(a)
                else:
                    edge[a].append(b + n)
                    edge[b].append(a + n)
            else:
                if cls[b] == 0:
                    edge[a + n].append(b + n)
                    edge[b].append(a)
                elif cls[b] == 1:
                    edge[a].append(b + n)
                    edge[b].append(a + n)
                else:
                    edge[a].append(b + n)
                    edge[b].append(a + n)
                    edge[a + n].append(b)
                    edge[b + n].append(a)

    def dfs(now):
        nonlocal count, scc_count
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

    for i in range(1, n * 2 + 1):
        if num[i] == 0: dfs(i)

    for i in range(1, n + 1):
        if scc_num[i] == scc_num[i + n]: return 0

    return 1

s, e = 0, n - 1
while s < e:
    m = (s + e) // 2
    if sat(m): e = m
    else: s = m + 1
while sat(s) == 0:
    s += 1
print(s)