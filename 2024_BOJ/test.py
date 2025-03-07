n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
check = [0] * (n + 1)       # 탐색 여부를 관리합니다.
dfs_count = 1               # 현재 탐색 번호
articulation_point = set()  # 단절점을 저장합니다.
s = 1                       # 탐색을 시작할 정점의 번호
root_count = 0              # 출발 지점의 하위 탐색 정점 개수


def dfs(now):
    global dfs_count
    check[now] = dfs_count
    near = dfs_count
    dfs_count += 1
    for next in graph[now]:
        # 탐색 번호가 더 빠른 정점으로 돌아갈 수 있는지 확인
        if check[next] and near > check[next]:
            near = check[next]

        # 탐색한 적 없는 정점이 있는 경우
        elif check[next] == 0:
            if now == s:
                global root_count
                root_count += 1
            sub = dfs(next)  # 하위 정점으로 출발한 탐색에서
            # 탐색 번호가 가장 빠른 정점을 찾습니다.

            # 탐색 번호가 더 빠른 정점으로 연결되는 경우
            if check[now] > sub:
                near = min(near, sub)

            # 탐색결과 돌아갈 수 있는 가장 빠른 탐색 번호가
            # 자기 자신이거나 그보다 나중 정점인 경우
            # 단절점이 되는 것으로 판정
            else:
                if now != s:
                    articulation_point.add(now)
    return near

dfs(1)
if root_count > 1:
    articulation_point.add(s)

print(articulation_point)