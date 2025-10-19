import sys
input = sys.stdin.readline
n, m = map(int, input().split())
K = set(map(int, input().split()))

link = [[] for _ in range(n + 1)]
match = [-1] * (n + 1)
for i in range(1, n + 1):
    if i in K: continue
    if i - 1 > 0 and not(i - 1 in K):
        link[i].append(i - 1)
    if i + 1 <= n and not(i + 1 in K):
        link[i].append(i + 1)
    if (i * 3) - 1 <= n and not((i * 3) - 1 in K):
        link[i].append((i * 3) - 1)
        link[(i * 3) - 1].append(i)

def dfs(a):
    if visit[a]: return 0
    visit[a] = 1
    for b in link[a]:
        if match[b] == -1:
            match[b] = a
            match[a] = b
            return 1
        elif dfs(match[b]):
            match[b] = a
            match[a] = b
            return 1
    visit[a] = 0
    return 0

count = 0
for i in range(1, n + 1):
    visit = [0] * (n + 1)
    if i in K or match[i] > 0: continue
    count += dfs(i)
print(n - count - m)