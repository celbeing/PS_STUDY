from collections import deque
import sys

input = sys.stdin.readline

MAX_H = 1000
MAX_W = 1000
MAX_Y = 100000


def main():
    h, w, n = map(int, input().split())
    ans = h * w
    a = [list(map(int, input().split())) for _ in range(h)]
    inland = [[True] * w for _ in range(h)]
    q = [deque() for _ in range(MAX_Y + 1)]

    for i in range(h):
        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                q[a[i][j]].append((i, j))
                inland[i][j] = False

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(1, n + 1):
        while q[i]:
            ans -= 1
            x, y = q[i].popleft()
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < h and 0 <= ny < w and inland[nx][ny]:
                    q[max(a[nx][ny], i)].append((nx, ny))
                    inland[nx][ny] = False
        print(ans)


if __name__ == "__main__":
    main()
