# 1017: 소수 쌍
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v):
    capa[u][v] = 1
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0
    return

sieve = [1] * 2001
prime = set()
sieve[0] = 0
sieve[1] = 0
for i in range(2, 2001):
    if sieve[i]:
        prime.add(i)
        for j in range(i * i, 2001, i):
            sieve[j] = 0

n = int(input())
a = list(map(int, input().split()))
flag = False
if a[0] & 1: pass
else:
    flag = True
    for i in range(n):
        if a[i] & 1: a[i] += 1
        else: a[i] -= 1

res = []
need_check = []

odd = []
even = []
capa = [dict() for _ in range(n + 2)]
flow = [dict() for _ in range(n + 2)]

for i in range(1, n):
    if a[i] & 1:
        odd.append(i)
        link(n, i)
    else:
        even.append(i)
        link(i, n + 1)
for e in even:
    if a[0] + a[e] in prime:
        need_check.append(e)

for o in odd:
    for e in even:
        if a[o] + a[e] in prime:
            link(o, e)

for t in need_check:
    capa[t][n + 1] = 0
    for now in range(n + 2):
        for next in flow[now]:
            flow[now][next] = 0

    total = 0
    while 1:
        bfs = deque([n])
        visit = [-1] * (n + 2)
        visit[n] = 0
        while bfs:
            now = bfs.popleft()
            for next in capa[now]:
                if capa[now][next] - flow[now][next] > 0 and visit[next] == -1:
                    visit[next] = now
                    bfs.append(next)
                    if next == n + 1:
                        bfs.clear()
                        break
        if visit[n + 1] == -1: break

        f = INF
        r = n + 1
        while r != n:
            f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
            r = visit[r]

        r = n + 1
        while r != n:
            flow[visit[r]][r] += f
            flow[r][visit[r]] -= f
            r = visit[r]

        total += f
    if total == (n - 1) // 2:
        res.append(a[t])

    capa[t][n + 1] = 1

if flag:
    for i in range(len(res)):
        res[i] -= 1
res.sort()
if res:
    print(*res)
else:
    print(-1)