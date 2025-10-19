from collections import deque

def sol2(r, c, grid):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dist = [[-1] * c for _ in range(r)]
    dist[0][0] = 0
    bfs = deque([(0, 0)])
    while bfs:
        x, y = bfs.popleft()
        if x == r - 1 and y == c - 1: break

        for k in range(4):
            nx, ny = x + d[k][0], y + d[k][1]
            while 1:
                if not(0 <= nx < r and 0 <= ny < c) or grid[nx][ny] == '#':
                    nx -= d[k][0]
                    ny -= d[k][1]
                    break
                elif grid[nx][ny] == '.':
                    nx += d[k][0]
                    ny += d[k][1]
                elif grid[nx][ny] == 'x':
                    break
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                bfs.append((nx, ny))
    return dist[-1][-1]

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
print(sol2(r, c, grid))