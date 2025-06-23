# 25488: 토큰
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dfs(now):
    global count
    count += 1
    visit[now] = 1
    num[now], low[now] = count, count
    stack.append(now)

    for next in edge[now]:
        if num[next] == 0:
            if dfs(next):
                return 1
            low[now] = min(low[now], low[next])
        elif visit[next]:
            low[now] = min(low[now], num[next])

    if num[now] == low[now]:
        red, blue = 0, 0
        while stack:
            c = stack.pop()
            visit[c] = 0
            if c in r: red += 1
            if c in b: blue += 1
            if c == now: break
        if red != blue: return 1
    return 0

n, m = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
p = int(input())
r = set(map(int, input().split()))
b = set(map(int, input().split()))

count = 0
visit, num, low = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
stack = []

for i in range(1, n + 1):
    if num[i] == 0 and dfs(i):
        print('NO')
        break
else:
    print('YES')