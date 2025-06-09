# 2416: 문
import sys
from array import array

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
node = m * 2 + 1
scc_num = array('I', [0]) * node
visit = array('I', [0]) * node
low = array('I', [0]) * node
num = array('I', [0]) * node
stack = []
count = 0
scc_count = 1

edge = [[] for _ in range(node)]
for _ in range(n):
    a, sa, b, sb = map(int, input().split())
    if sa == 0: a *= -1
    if sb == 0: b *= -1
    edge[-a].append(b)
    edge[-b].append(a)

def dfs(now):
    global count, scc_count
    count += 1
    stack.append(now)
    visit[now] = count
    low[now] = count
    num[now] = count

    for next in edge[now]:
        if scc_num[next]: continue
        if num[next] == 0:
            dfs(next)
            if low[now] > low[next]: low[now] = low[next]
        elif visit[next]:
            if low[now] > num[next]: low[now] = num[next]

    if low[now] == num[now]:
        while stack:
            t = stack.pop()
            visit[t] = 0
            scc_num[t] = scc_count
            if now == t: break
        scc_count += 1

for i in range(-m, m + 1):
    if i == 0: continue
    if num[i] == 0: dfs(i)

poss = True
res = array('I', [0]) * (m + 1)
for i in range(1, m + 1):
    if scc_num[i] == scc_num[-i]:
        poss = False
        break
    elif scc_num[i] < scc_num[-i]:
        res[i] = 1

if poss:
    for i in range(1, m + 1):
        print(res[i])
else:
    print('IMPOSSIBLE')