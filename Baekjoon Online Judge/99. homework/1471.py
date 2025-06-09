# 1471: 사탕 돌리기
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def digit_sum(k):
    ret = 0
    while k:
        ret += k % 10
        k //= 10
    return ret

def scc(now):
    global count
    count += 1

    stack.append(now)
    dfs_num[now] = count
    visit[now] = 1
    back[now] = count

    next = edge[now]
    if dfs_num[next] == 0:
        scc(next)
        back[now] = min(back[now], back[next])
    elif visit[next]:
        back[now] = min(back[now], dfs_num[next])

    if back[now] == dfs_num[now]:
        comp = []
        while stack:
            comp.append(stack.pop())
            visit[comp[-1]] = 0
            if now == comp[-1]: break

        scc_size = len(comp)
        if scc_size > 1:
            for c in comp:
                dp[c] = scc_size

def dfs(now):
    next = edge[now]
    if now == next:
        dp[now] = 1
    elif dp[next] > -1:
        dp[now] = dp[next] + 1
    else:
        dp[now] = dfs(next) + 1

    return dp[now]

n = int(input())
edge = [0] * (n + 1)
for now in range(1, n + 1):
    next = (now + digit_sum(now)) % n
    edge[now] = next if next else n

stack = []
dfs_num = [0] * (n + 1)
visit = [0] * (n + 1)
back = [0] * (n + 1)
dp = [-1] * (n + 1)
count = 0

for i in range(1, n + 1):
    if dfs_num[i] == 0: scc(i)

for i in range(1, n + 1):
    if dp[i] == -1: dfs(i)

print(max(dp))