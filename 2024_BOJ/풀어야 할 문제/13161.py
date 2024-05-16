# 13161: 분단의 슬픔
import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)

N = int(input())
camp = list(map(int,input().split()))
graph = [[] for _ in range(N+2)]
for i in range(1,N+1):
    if camp[i-1] == 1: graph[0].append((i,inf))
    elif camp[i-1] == 2: graph[i].append((N+1,inf))
    capa = list(map(int,input().split()))
    for j in range(1,N+1):
        if capa[j-1] > 0:
            graph[i].append((j,capa[j-1]))

flow = [[0]*(N+2) for _ in range(N+2)]
work = [0]*(N+2)
level = [-1]*(N+2)

result = 0
while True:
    # 레벨 그래프 생성
    for i in range(N+2): level[i] = -1
    level[0] = 0
    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        for next,capa in graph[now]:
            if level[next] == -1 and capa - flow[now][next] > 0:
                level[next] = level[now] + 1
                bfs.append(next)
    if level[-1] == -1: break

    # 유량 생성
    for i in range(N+2): work[i] = 0
    while True:
        stack = [(0, inf)]
        while stack:
            now, cut = stack[-1]
            if now == N + 1:
                for i in range(len(stack) - 1):
                    flow[stack[i][0]][stack[i + 1][0]] += cut
                    flow[stack[i + 1][0]][stack[i][0]] -= cut
                result += cut
                break
            for i in range(work[now], len(graph[now])):
                work[now] += 1
                next = graph[now][i][0]
                capa = graph[now][i][1]
                residual = capa - flow[now][next]
                if residual > 0 and level[now] + 1 == level[next]:
                    f = min(residual, cut)
                    stack.append((next, f))
                    break
            else:
                stack.pop()
        else:
            break

print(result)

visited = [False]*(N+2)
visited[0] = True
bfs = deque([0])
while bfs:
    now = bfs.popleft()
    for next,capa in graph[now]:
        if not(visited[next]) and capa-flow[now][next] > 0:
            visited[next] = True
            bfs.append(next)
A = []
B = []
for i in range(1,N+1):
    if visited[i]: A.append(i)
    else: B.append(i)
print(*A)
print(*B)