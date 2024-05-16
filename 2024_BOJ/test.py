# 13161: 분단의 슬픔
import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)

N = int(input())
camp = list(map(int,input().split()))
capa = [[0]*(N+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+2)]
flow = [[0]*(N+2) for _ in range(N+2)]
work = [0]*(N+2)

# 유량 보내주기
def dfs(level, start, end, min_capacity):
    stack = [(start, min_capacity)]
    while stack:
        node, capacity = stack[-1]
        if node == end:
            return capacity
        for next_node in range(work[node], N + 2):
            work[node] += 1
            residual = capa[node][next_node] - flow[node][next_node]
            if residual > 0 and level[node] + 1 == level[next_node]:
                f = min(residual, capacity)
                stack.append((next_node, f))
                break
        else:
            stack.pop()
    return 0

result = 0
while True:
    level = [-1] * (N + 2)
    level[0] = 0
    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        for next_node in range(N + 2):
            if level[next_node] == -1 and capa[now][next_node] - flow[now][next_node] > 0:
                level[next_node] = level[now] + 1
                bfs.append(next_node)
    if level[-1] == -1:
        break

    work = [0] * (N + 2)
    while True:
        f = dfs(level, 0, N + 1, inf)
        if f == 0:
            break
        result += f

print(result)

visited = [False] * (N + 2)
visited[0] = True
bfs = deque([0])
while bfs:
    now = bfs.popleft()
    for next_node in range(N + 2):
        if not visited[next_node] and capa[now][next_node] - flow[now][next_node] > 0:
            visited[next_node] = True
            bfs.append(next_node)

A = [i for i in range(1, N + 1) if visited[i]]
B = [i for i in range(1, N + 1) if i not in A]
print(*A)
print(*B)
