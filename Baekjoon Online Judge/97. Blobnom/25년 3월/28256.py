# 28256: 초콜릿 보관함
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for _ in range(int(input())):
        case = [list(input().strip()) for _ in range(3)]
        check = [[0] * 3 for _ in range(3)]
        count = []
        bfs = deque()
        for i in range(3):
            for j in range(3):
                if case[i][j] == 'O' and check[i][j] == 0:
                    bfs.append((i, j))
                    check[i][j] = 1
                    count.append(1)
                    while bfs:
                        x, y = bfs.popleft()
                        for k in range(4):
                            dx, dy = x + d[k][0], y + d[k][1]
                            if 0 <= dx < 3 and 0 <= dy < 3 and case[dx][dy] == 'O' and check[dx][dy] == 0:
                                check[dx][dy] = 1
                                bfs.append((dx, dy))
                                count[-1] += 1
        a = list(map(int, input().split()))[1:]
        count.sort()
        if a == count:
            print(1)
        else:
            print(0)
solution()