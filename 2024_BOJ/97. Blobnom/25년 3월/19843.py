# 19843: 수면 패턴
import sys
input = sys.stdin.readline
def solution():
    t, n = map(int, input().split())
    week = {'Mon': 0, 'Tue': 24, 'Wed': 48, 'Thu': 72, 'Fri': 96}
    for _ in range(n):
        d1, h1, d2, h2 = map(str, input().split())
        h1, h2 = int(h1), int(h2)
        t -= week[d2] + h2 - week[d1] - h1
    if t > 48:
        print(-1)
    elif t < 0:
        print(0)
    else:
        print(t)
solution()