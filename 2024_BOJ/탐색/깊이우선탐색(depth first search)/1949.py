#1949: 우수 마을
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())
p = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
take = [0 for _ in range(N+1)]
drop = [0 for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    take[node] += p[node]
    while graph[node]:
        next = graph[node].pop()
        if take[next] > 0: continue
        dfs(next)
        take[node] += drop[next]
        drop[node] += max(drop[next], take[next])
    return

dfs(1)
print(max(drop[1],take[1]))