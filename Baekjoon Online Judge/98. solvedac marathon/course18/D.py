#2589: 보물섬
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    height, width = map(int, input().split())
    treasure_map = [tuple(input().rstrip()) for _ in range(height)]
    bfs = deque()
    result = 0
    for i in range(height):
        for j in range(width):
            if treasure_map[i][j] == "L":
                bfs.append((i, j))
                visit = [[-1] * width for _ in range(height)]
                visit[i][j] = 0
                x, y = 0, 0
                while bfs:
                    x, y = bfs.popleft()
                    for k in range(4):
                        dx = x + d[k][0]
                        dy = y + d[k][1]
                        if 0 <= dx < height and 0 <= dy < width and treasure_map[dx][dy] == "L" and visit[dx][dy] == -1:
                            bfs.append((dx, dy))
                            visit[dx][dy] = visit[x][y] + 1
                if visit[x][y] > result:
                    result = visit[x][y]
    print(result)
solution()