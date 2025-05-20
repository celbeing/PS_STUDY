# 9738: Sharkovski’s Ordering
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        b = []
        for k in a:
            if k == 0: break
            t = k
            c = 0
            while not(t & 1):
                t >>= 1
                c += 1
            if t <= 1:
                t = int(1e5)
                c *= -1
                c += 255
            b.append((c, t, k))
        b.sort(key = lambda x: (x[0], x[1]))
        res = []
        for x, y, z in b:
            res.append(z)
        print(*res)
solution()