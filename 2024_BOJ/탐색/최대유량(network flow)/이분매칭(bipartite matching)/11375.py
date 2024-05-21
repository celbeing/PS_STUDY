# 11375: 열혈강호
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    task = list(map(int, input().split()))
    for j in range(1, task[0] + 1):
        graph[i].append(task[j] - 1)
match = [-1]*M

def bipartite(k):
    if visit[k]: return False
    visit[k] = True
    for t in graph[k]:
        if match[t] == -1:
            match[t] = k
            return True
    for t in graph[k]:
        if match[t]>= 0 and bipartite(match[t]):
            match[t] = k
            return True
    return False

count = 0
for i in range(N):
    visit = [False] * N
    if bipartite(i): count += 1
    if count == M: break # 시간초과 예방에 아주 효과적..!!

print(count)