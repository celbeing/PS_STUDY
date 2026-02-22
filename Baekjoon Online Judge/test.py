<<<<<<< HEAD
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

n, p = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
tree = [set() for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].add(v)
    tree[v].add(u)
check = [0] * (n + 1)

def DFS(now):
    check[now] = 1
    need = 0
    for nxt in tree[now]:
        if check[nxt] == 0:
            need += DFS(nxt)
    need -= a[now] - b[now]
    if need < 0: need = 0
    return need

result = DFS(p)
print(result)
=======
n = int(input())
if n in (1, 3): print(-1)
else:
    dp = [int(1e9) if i & 1 else i // 2 for i in range(n + 1)]
    for i in range(5, n + 1):
        dp[i] = min(dp[i], dp[i - 5] + 1)
    print(dp[n])
>>>>>>> b6efd420b4b681c06d7f104d16d42bee12776b75
