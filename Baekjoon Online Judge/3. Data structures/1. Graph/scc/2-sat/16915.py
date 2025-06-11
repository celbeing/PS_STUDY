# 16915: 호텔 관리
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, m = map(int, input().split())
door = [0] + list(map(int, input().split()))
link = [0] * (n + 1)
node = m * 2 + 1
edge = [[] for _ in range(node)]
for i in range(1, m + 1):
    switch = list(map(int, input().split()))
    for d in switch[1:]:
        if link[d]:
            j = link[d]
            if door[d]:
                edge[i].append(j)
                edge[j].append(i)
                edge[-i].append(-j)
                edge[-j].append(-i)
            else:
                edge[-i].append(j)
                edge[j].append(-i)
                edge[-j].append(i)
                edge[i].append(-j)
        else:
            link[d] = i

stack = []
count = 0
visit = [0] * node
num = [0] * node
low = [0] * node
scc_num = [0] * node
scc_count = 1

def dfs(now):
    global count, scc_count
    count += 1
    num[now] = count
    low[now] = count
    visit[now] = 1
    stack.append(now)

    for next in edge[now]:
        if num[next] == 0:
            dfs(next)
            low[now] = min(low[now], low[next])
        elif visit[next]:
            low[now] = min(low[now], num[next])

    if low[now] == num[now]:
        while stack:
            t = stack.pop()
            visit[t] = 0
            scc_num[t] = scc_count
            if t == now: break
        scc_count += 1

for i in range(-m, m + 1):
    if i and num[i] == 0: dfs(i)

flag = True
res = [0] * (m + 1)
for i in range(1, m + 1):
    if scc_num[i] == scc_num[-i]:
        flag = False
        break
    elif scc_num[i] < scc_num[-i]:
        res[i] = 1

print(1 if flag else 0)