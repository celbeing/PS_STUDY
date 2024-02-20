#2533: 사회망 서비스(SNS)
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
take = [0 for _ in range(N+1)]
drop = [0 for _ in range(N+1)]

for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    take[node] += 1
    while graph[node]:
        next = graph[node].pop()
        if take[next] > 0: continue
        dfs(next)
        take[node] += min(drop[next],take[next])
        drop[node] += take[next]
    return

dfs(1)

print(min(take[1],drop[1]))