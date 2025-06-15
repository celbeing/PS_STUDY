# 1739: 도로 정비하기
import sys
sys.setrecursionlimit(4001)
input = sys.stdin.readline

def neg(k): return k + 2000 if k <= 2000 else k - 2000

t = int(input())

def solution():
    n, m, k = map(int, input().split())
    edge = [[] for _ in range(4001)]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        if a == c and b == d: continue
        b, d = b + 1000, d + 1000
        if a == c:
            if b < d:
                edge[neg(a)].append(a)
            else:
                edge[a].append(neg(a))
        elif b == d:
            if a < c:
                edge[neg(b)].append(b)
            else:
                edge[b].append(neg(b))
        else:
            if a > c: b, d = neg(b), neg(d)
            if b > d: a, c = neg(a), neg(c)
            edge[neg(a)].append(b)
            edge[neg(b)].append(a)
            edge[neg(a)].append(c)
            edge[neg(c)].append(a)
            edge[neg(d)].append(b)
            edge[neg(b)].append(d)
            edge[neg(d)].append(c)
            edge[neg(c)].append(d)

    count, scc_count = 0, 0
    visit = [0] * 4001
    num = [0] * 4001
    low = [0] * 4001
    scc_num = [0] * 4001
    stack = []

    def dfs(now):
        nonlocal count, scc_count
        count += 1
        stack.append(now)
        visit[now] = 1
        num[now] = low[now] = count

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
                if now == c: break

    for i in range(1, n + 1):
        if num[i] == 0: dfs(i)
        if num[neg(i)] == 0: dfs(neg(i))
    for i in range(1001, m + 1001):
        if num[i] == 0: dfs(i)
        if num[neg(i)] == 0: dfs(neg(i))

    for i in range(1, n + 1):
        if scc_num[i] == scc_num[neg(i)]: break
    else:
        for j in range(1001, m + 1001):
            if scc_num[j] == scc_num[neg(j)]: break
        else:
            print('Yes')
            return
    print('No')
    return

for _ in range(t):
    solution()