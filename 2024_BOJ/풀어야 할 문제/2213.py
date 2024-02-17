#2213: 트리의 독립집합
import sys
input = sys.stdin.readline
n = int(input())
w = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
	u,v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)
take = [0 for _ in range(n+1)]
take_path = [[] for _ in range(n+1)]
drop = [0 for _ in range(n+1)]
drop_path = [[] for _ in range(n+1)]

def dfs(parent,node):
	if len(graph[node]) == 1:
		take[node] = w[node]
		take_path[node].append(node)
		return
	while graph[node]:
		next = graph[node].pop()
		if next == parent: continue
		dfs(node,next)
		take[node] = drop[next] + w[node]
		drop[node] =