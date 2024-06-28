# 11014: 컨닝 2
import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)
d = [(-1,-1),(0,-1),(1,-1),(-1,1),(0,1),(1,1)]

def bipartite(k):
    if visit[k]: return 0
    visit[k] = 1
    for t in graph[k]:
        if not(match[t]):
            match[t] = k
            return 1
    for t in graph[k]:
        if bipartite(match[k]):
            match[k] = t
            return 1
    return 0

C = int(input())
for _ in range(C):
    N,M = map(int,input().split())
    graph = [[] for _ in range((M+1)*N//2)]
    room = [list(input().rstrip()) for _ in range(N)]
    seat = 0
    for i in range(N):
        for j in range(M):
            if room[i][j] == '.': seat += 1

    for i in range(N):
        for j in range(0,M,2):
            if room[i][j] == '.':
                for k in range(6):
                    di,dj = i+d[k][0],j+d[k][1]
                    if 0<=di<N and 0<=dj<M and room[di][dj] == '.':
                        graph[j*N//2+i].append((dj-1)*N//2+di)
    match = [0]*(M//2*N)
    count = 0
    for i in range(M//2*N):
        visit = [0]*((M+1)//2*N)
        count += bipartite(i)
    print(seat-count)