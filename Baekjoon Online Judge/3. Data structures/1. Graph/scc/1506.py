# 1506: 경찰서
import sys
input = sys.stdin.readline

def dfs(now):
    global count, total
    count += 1
    visit[now] = 1
    num[now], low[now] = count, count
    stack.append(now)

    for next in edge[now]:
        if num[next] == 0:
            dfs(next)
            low[now] = min(low[now], low[next])
        elif visit[next]:
            low[now] = min(low[now], num[next])

    if num[now] == low[now]:
        police = 10**6
        while stack:
            c = stack.pop()
            visit[c] = 0
            if cost[c] < police:
                police = cost[c]
            if c == now: break
        total += police


n = int(input())
cost = list(map(int, input().split()))
road = [list(input().strip()) for _ in range(n)]
edge = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if road[i][j] == '1':
            edge[i].append(j)

count, total = 0, 0
visit = [0] * n
num, low = [0] * n, [0] * n
stack = []

for i in range(n):
    if num[i] == 0: dfs(i)

print(total)