# 11839: Beautiful row
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

def one_counter(k):
    t = k
    binary, tenary = 0, 0
    while t:
        if t & 1: binary += 1
        t >>= 1
    t = k
    while t:
        if t % 3 == 1: tenary += 1
        t //= 3
    return (binary, tenary)

count = []
link = [[] for _ in range(n + 1)]
link[n] = [i for i in range(n)]
for i in range(n):
    count.append(one_counter(p[i]))
    for j in range(i):
        if count[i][0] == count[j][0] or count[i][1] == count[j][1]:
            link[i].append(j)
            link[j].append(i)

dp = [[-1] * (1 << (n + 1)) for _ in range(n + 1)]
for i in range(n):
    dp[i][(1 << (n + 1)) - 1] = 1

def tsp(now, visit):
    if dp[now][visit] == -1:
        ret = 0
        for next in link[now]:
            if visit & 1 << next: continue
            ret += tsp(next, visit | (1 << next))
        dp[now][visit] = ret
    return dp[now][visit]

print(tsp(n, 1 << n))