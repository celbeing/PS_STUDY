# 14575: 뒤풀이
import sys
input = sys.stdin.readline
def solution():
    n, t = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    maxsum = 0
    minimum = 1000000
    minsum = t
    for l, r in lr:
        maxsum += r
        minsum -= l
        minimum = min(l, minimum)
    if maxsum < t:
        print(-1)
        return
    s, e = minimum, t + 1
    while s < e:
        m = (s + e) // 2
        need = 0
        for l, r in lr:
            need += min(r, m) - l

        if need < minsum:
            s = m + 1
        else:
            e = m
    print(s)
solution()