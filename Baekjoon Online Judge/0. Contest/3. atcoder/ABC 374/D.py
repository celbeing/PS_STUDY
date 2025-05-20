import sys
input = sys.stdin.readline
def find(N, graph, visit, now, dist, depth):
    res = 1e9
    if depth == N: return dist
    for i in range(N):
        if visit[i]: continue
        visit[i] = 1
        res = min(res, find(N, graph, visit, i*2+1, dist + graph[now][i*2] + graph[i*2][i*2+1], depth + 1))
        res = min(res, find(N, graph, visit, i*2, dist + graph[now][i*2+1] + graph[i*2+1][i*2], depth + 1))
        visit[i] = 0
    return res
def solution():
    N, S, T = map(int, input().split())
    graph = [[1e9] * (N*2) for _ in range(N*2)]
    loc = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        graph[i*2][i*2+1] = ((loc[i][0] - loc[i][2])**2 + (loc[i][1] - loc[i][3])**2)**0.5/T
        graph[i*2+1][i*2] = graph[i*2][i*2+1]
        for j in range(i + 1, N):
            graph[i*2][j*2] = ((loc[i][0]-loc[j][0])**2 + (loc[i][1] - loc[j][1])**2)**0.5/S
            graph[i*2+1][j*2] = ((loc[i][2]-loc[j][0])**2 + (loc[i][3] - loc[j][1])**2)**0.5/S
            graph[i*2][j*2+1] = ((loc[i][0]-loc[j][2])**2 + (loc[i][1] - loc[j][3])**2)**0.5/S
            graph[i*2+1][j*2+1] = ((loc[i][2]-loc[j][2])**2 + (loc[i][3] - loc[j][3])**2)**0.5/S
            graph[j*2][i*2] = graph[i*2][j*2]
            graph[j*2][i*2+1] = graph[i*2+1][j*2]
            graph[j*2+1][i*2] = graph[i*2][j*2+1]
            graph[j*2+1][i*2+1] = graph[i*2+1][j*2+1]
    res = 1e9
    for i in range(N):
        visit = [0]*N
        visit[i] = 1
        res = min(res, find(N, graph, visit, i*2+1, (loc[i][0]**2+loc[i][1]**2)**0.5/S+graph[i*2][i*2+1], 1))
        res = min(res, find(N, graph, visit, i*2, (loc[i][2]**2+loc[i][3]**2)**0.5/S+graph[i*2+1][i*2], 1))
        visit[i] = 0
    print(res)
solution()