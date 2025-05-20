#25516: 거리가 k이하인 4. Tree 노드에서 사과 수확하기
import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    p,c = map(int,input().split())
    graph[p].append(c)
check = [-1] * n
check[0] = 0
bfs = deque()
bfs.append(0)
apple = list(map(int,input().split()))
result = 0
while bfs:
    now = bfs.popleft()
    if apple[now] == 1 and check[now] <= k:
        result += 1
    for next in graph[now]:
        if check[next] == -1:
            check[next] = check[now] + 1
            bfs.append(next)
print(result)