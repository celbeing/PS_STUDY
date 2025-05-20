#1025: 제곱수 찾기
import sys
input = sys.stdin.readline
def is_power(k):
    return True if k == (int(k**0.5))**2 else False
def solution():
    N, M = map(int, input().split())
    res = -1
    table = [list(input().rstrip()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            table[i][j] = int(table[i][j])
    for i in range(N):
        for j in range(M):
            for x in range(-i, N - i):
                for y in range(-j, M - j):
                    n = table[i][j]
                    if x == 0 and y == 0:
                        if is_power(n) and n > res: res = n
                        continue
                    dx = i + x
                    dy = j + y
                    while 0 <= dx < N and 0 <= dy < M:
                        n = n * 10 + table[dx][dy]
                        if is_power(n) and n > res: res = n
                        dx += x
                        dy += y
    print(res)
solution()