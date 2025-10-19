from collections import deque

def sol(r, c, grid):
    check = [[-1] * c for _ in range(r)]
    graph = get_graph(r, c, grid)
    bfs = deque([(0, 0)])
    check[0][0] = 0
    while bfs:
        x, y = bfs.popleft()
        if x == r - 1 and y == c - 1: break
        for nx, ny in graph[x][y]:
            if check[nx][ny] == -1:
                check[nx][ny] = check[x][y] + 1
                bfs.append((nx, ny))
    return check[-1][-1]

def get_graph(r, c, grid):
    # 상, 하, 좌, 우
    graph = [[[(0, 0)] * 4 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        tx, ty = i, 0
        for j in range(c):
            if grid[i][j] == '#':
                ty = j + 1
            elif grid[i][j] == 'x':
                graph[i][j][2] = (tx, ty)
                ty = j
            else:
                graph[i][j][2] = (tx, ty)

    for i in range(r):
        tx, ty = i, c - 1
        for j in range(c - 1, -1, -1):
            if grid[i][j] == '#':
                ty = j - 1
            elif grid[i][j] == 'x':
                graph[i][j][3] = (tx, ty)
                ty = j
            else:
                graph[i][j][3] = (tx, ty)

    for j in range(c):
        tx, ty = 0, j
        for i in range(r):
            if grid[i][j] == '#':
                tx = i + 1
            elif grid[i][j] == 'x':
                graph[i][j][0] = (tx, ty)
                tx = i
            else:
                graph[i][j][0] = (tx, ty)

    for j in range(c):
        tx, ty = r - 1, j
        for i in range(r - 1, -1, -1):
            if grid[i][j] == '#':
                tx = i - 1
            elif grid[i][j] == 'x':
                graph[i][j][1] = (tx, ty)
                tx = i
            else:
                graph[i][j][1] = (tx, ty)

    return graph

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
print(sol(r, c, grid))