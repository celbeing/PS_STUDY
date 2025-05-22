# 5130: B1 부여 궁남지 연꽃 키우기 1
import sys
from collections import deque

def solution():
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    h, w = map(int, input().split())
    pond = [[-1] * w for _ in range(h)]
    x, y = map(int, input().split())
    n = int(input())
    pond[x][y] = 0
    day = 0
    day_count = 1
    bfs = deque([(x, y)])
    while day < n:
        new_count = 0
        for _ in range(day_count):
            x, y = bfs.popleft()
            for k in range(4):
                nx = x + d[k][0]
                ny = y + d[k][1]
                if 0 <= nx < h and 0 <= ny < w and pond[nx][ny] <= day:
                    pond[nx][ny] = day + 1
                    new_count += 1
                    bfs.append((nx, ny))
        day_count = new_count
        day += 1
    print(day_count)
solution()