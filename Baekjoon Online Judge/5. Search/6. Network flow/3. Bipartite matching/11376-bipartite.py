# 11376: 열혈강호 2
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [0]
for _ in range(N):
    task = list(map(int,input().split()))[1:]
    graph.append(task)
    graph.append(task)
match = [0]*(M+1)

def dfs(k):
    if visit[k]: return 0
    visit[k] = 1
    for t in graph[k]:
        if not(match[t]):
            match[t] = k
            return 1
    for t in graph[k]:
        if dfs(match[t]):
            match[t] = k
            return 1
    return 0

count = 0
for i in range(1,N*2+1):
    visit = [0]*(N*2+1)
    count += dfs(i)
    if count == M: break

print(count)