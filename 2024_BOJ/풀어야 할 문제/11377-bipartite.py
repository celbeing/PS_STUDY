# 11377: 열혈강호 3-이분매칭
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
mono = [[]]
doub = [[]]
for _ in range(N):
    task = list(map(int,input().split()))[1:]
    mono.append(task)
    doub.append(task)
match = [0]*(M+1)

def dfs1(k):
    if visit[k]: return 0
    visit[k] = 1
    for t in mono[k]:
        if not(match[t]):
            match[t] = k
            return 1
    for t in mono[k]:
        if dfs1(match[k]):
            match[k] = t
            return 1
    return 0

def dfs2(k):
    if visit[k]: return 0
    visit[k] = 1
    for t in doub[k]:
        if not(match[t]):
            match[t] = k
            return 1
    for t in doub[k]:
        if dfs2(match[k]):
            match[k] = t
            return 1
    return 0

result = 0
count = 0
for i in range(1,N+1):
    visit = [0]*(N+1)
    count += dfs1(i)
    if count == N: break
result += count

count = 0
for i in range(1,N+1):
    visit = [0]*(N+1)
    count += dfs2(i)
    if count == K: break
result += count

print(result)