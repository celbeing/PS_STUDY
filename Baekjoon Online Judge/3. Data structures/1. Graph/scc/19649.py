# 19649: 미담 전하기
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
k = int(input())

scc = []
count = 0

stack = []
dfs_num = [0] * (n + 1)
visit = [0] * (n + 1)
back = [0] * (n + 1)

dp = [(0, 0)] * (n + 1)

def dfs(now):
    global count
    count += 1
    stack.append(now)
    visit[now] = 1
    back[now] = count
    dfs_num[now] = count

    for next in edge[now]:
        if dfs_num[next] == 0:
            dfs(next)
            back[now] = min(back[now], back[next])
        elif visit[next]:
            back[now] = min(back[now], dfs_num[next])

    if back[now] == dfs_num[now]:
        comp = []
        while stack:
            comp.append(stack.pop())
            visit[comp[-1]] = 0
            if now == comp[-1]: break
        comp.sort()
        scc.append(comp)

for i in range(1, n + 1):
    if dfs_num[i] == 0:
        dfs(i)

is_alone = 0

while scc:
    s = scc.pop()
    l = len(s)
    if l == 1 and s[0] == k:
        is_alone = 1
    for now in s:
        dp[now] = (dp[now][0] + l, dp[now][1] if dp[now][1] else (s[0] if k != s[0] else s[1]))
        visit[now] = 1
    for now in s:
        for next in edge[now]:
            if visit[next]: continue
            if dp[next][0] < dp[now][0]:
                dp[next] = dp[now]
            elif dp[next][0] == dp[now][0] and dp[next][1] > dp[now][1]:
                dp[next] = dp[now]
res = 0 if dp[k][1] == k else dp[k][0] - 1 - is_alone
if res == 0:
    print(0)
else:
    print(dp[k][1], res)