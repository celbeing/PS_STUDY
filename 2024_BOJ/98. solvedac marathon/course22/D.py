#1640: 동전 뒤집기
import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    v = [0] * M
    h = [0] * N
    for i in range(N):
        row = list(input().strip())
        for j in range(M):
            if row[j] == "1":
                v[j] = 0 if v[j] else 1
                h[i] = 0 if h[i] else 1

    v = sum(v)
    h = sum(h)

    res = 0
    if N & 1 and M & 1:
        if v & 1 and h & 1:
            res = min(v + N - h, h + M - v)
        else:
            res = min(v, h)
    elif N & 1:

    print(res)
solution()