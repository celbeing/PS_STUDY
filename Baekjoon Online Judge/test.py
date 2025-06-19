import sys
input = sys.stdin.readline

def dfs(now):
    dp[now] = 1
    for next in edge[now]:
        if dp[next]: continue
        dfs(next)
        dp[now] += dp[next]

n = int(input())
dp = [0] * (n + 1)
edge = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

dfs(1)

node = 0
high = 0
for i in range(1, n + 1):
    res = 1
    for j in edge[i]:
        if dp[i] < dp[j]:
            res *= n - dp[i]
        else:
            res *= dp[j]
    if high < res:
        high = res
        node = i
print(node, high)