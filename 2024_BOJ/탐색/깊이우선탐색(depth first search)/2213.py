#2213: 트리의 독립집합
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
w = [0]+list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
	u,v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)
take = [0 for _ in range(n+1)]
take_path = [[] for _ in range(n+1)]
drop = [0 for _ in range(n+1)]
drop_path = [[] for _ in range(n+1)]

def dfs(node):
	take[node] += w[node]
	take_path[node].append(node)
	while graph[node]:
		next = graph[node].pop()
		if take[next] > 0: continue
		dfs(next)
		take[node] += drop[next]
		take_path[node] += drop_path[next]
		if take[next] > drop[next]:
			drop[node] += take[next]
			drop_path[node] += take_path[next]
		else:
			drop[node] += drop[next]
			drop_path[node] += drop_path[next]
	return

dfs(1)
if take[1] > drop[1]:
	print(take[1])
	print(*sorted(take_path[1]))
else:
	print(drop[1])
	print(*sorted(drop_path[1]))