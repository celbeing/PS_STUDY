from collections import deque

# v, e: 정점, 간선 수
# stack: dfs 스택
# edge: 간선 정보
# back: 되돌아갈 수 있는 정점
# dfs_num: dfs 방문 순서
# visit: 스택 포함 여부
# count: 현재 dfs 방문 순서 관리
# scc: scc 컴포넌트 관리

stack = deque()
back = [i for i in range(v + 1)]
dfs_num = [0] * (v + 1)
visit = [0] * (v + 1)
count = 0
scc = []

def dfs(now):
    global count
    count += 1
    stack.append(now)
    visit[now] = 1
    back = count
    dfs_num = count

    for next in edge[now]:
        if dfs_num[next] == 0:
            dfs(next)
            back[now] = min(back[now], back[next])
        elif visit[next]:
            back[now] = min(back[now], dfs_num[next])

    if back[now] == dfs_num[now]:
        comp = []
        while stack:
            comp.append(stack.pop())
            visit[comp[-1]] = 0
            if now == comp[-1]: break
        comp.sort()
        scc.append(comp)

for i in range(1, v + 1):
    if dfs_num[i] == 0: dfs(i)

scc.sort()