import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
edge = [set() for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edge[u].add(v)
    edge[v].add(u)

l = []
dq = deque([1])
check = [0] * (n + 1)
check[1] = 1
while True:
    now = dq.popleft()
    l.append(now)
    if len(l) == 4: break
    for nxt in edge[now]:
        if check[nxt]: continue
        dq.append(nxt)
        check[nxt] = 1

link = []
for i in range(3):
    for j in range(i + 1, 4):
        link.append((l[i], l[j]))

res = []
for a, b in link:
    if a in edge[b]: continue
    res.append((a, b))

print(len(res))
for a, b in res:
    print(a, b)