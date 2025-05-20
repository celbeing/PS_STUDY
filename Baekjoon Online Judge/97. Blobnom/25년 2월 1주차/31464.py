# 31464: 초콜릿 괴도 코코 (Sweet)
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution():
    n = int(input())
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    chocolate = [list(input().strip()) for _ in range(n)]
    non_artic_point = set()
    check = [[0] * n for _ in range(n)]
    dfs_count = 1

    def dfs(x, y):
        nonlocal dfs_count
        check[x][y] = dfs_count
        near = dfs_count
        dfs_count += 1
        root_count = 0
        is_artic_point = False
        for k in range(4):
            nx, ny = x + d[k][0], y + d[k][1]
            if 0 <= nx < n and 0 <= ny < n and chocolate[nx][ny] == '#':
                if check[nx][ny] and near > check[nx][ny]:
                    near = check[nx][ny]
                elif check[nx][ny] == 0:
                    if x == rx and y == ry: root_count += 1
                    sub = dfs(nx, ny)
                    if check[x][y] <= sub:
                        is_artic_point = True
                    elif sub < near:
                        near = sub
        if is_artic_point == False:
            non_artic_point.add((x, y))
        if x == rx and y == ry:
            return root_count
        return near

    rx, ry = -1, -1
    for i in range(n):
        for j in range(n):
            if chocolate[i][j] == '#':
                rx = i
                ry = j
                break
        if rx >= 0: break
    if dfs(rx, ry) == 1: non_artic_point.add((rx, ry))

    node = 0
    edge = [[0] * n for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):
            if chocolate[i][j] == '#':
                node += 1
                for k in range(4):
                    ni, nj = i + d[k][0], j + d[k][1]
                    if 0 <= ni < n and 0 <= nj < n and chocolate[ni][nj] == '#':
                        edge[i][j] += 1
                        total += 1
    node -= 2
    total //= 2
    result = []
    for x, y in non_artic_point:
        if total - edge[x][y] == node:
            result.append((x + 1, y + 1))

    if result:
        result.sort()
        print(len(result))
        for k in result:
            print(*k)
    else:
        print(0)

solution()