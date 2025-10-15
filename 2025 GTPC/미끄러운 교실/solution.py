from collections import deque

def sol(r, c, grid):
    graph = get_graph(r, c, grid)
    dist = [[-1] * c for _ in range(r)]
    dist[0][0] = 0
    bfs = deque([(0, 0)])
    while bfs:
        x, y = bfs.popleft()
        if x == r - 1 and y == c - 1: break
        for nx, ny in graph[x][y]:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                bfs.append((nx, ny))
    return dist[-1][-1]

def get_graph(r, c, grid):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    graph = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(4):
                x, y = i + d[k][0], j + d[k][1]
                while 1:
                    if not(0 <= x < r and 0 <= y < c) or grid[x][y] == '#':
                        if not(i == x - d[k][0] and j == y - d[k][1]):
                            graph[i][j].append((x - d[k][0], y - d[k][1]))
                        break
                    elif grid[x][y] == '.':
                        x += d[k][0]
                        y += d[k][1]
                    else:
                        graph[i][j].append((x, y))
                        break
    return graph

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
print(sol(r, c, grid))