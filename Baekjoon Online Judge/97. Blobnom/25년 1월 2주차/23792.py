# 23792: K번째 음식 찾기 2
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    food = [[0] + list(map(int, input().split())) for _ in range(3)]
    def find(a, b, c, x, y, z, k):
        s, e = 0, x
        while s <= e:
            m = (s + e) // 2
            sb, sc, eb, ec = 0, 0, y, z
            while sb < eb:
                mb = (sb + eb + 1) // 2
                if food[b][mb] <= food[a][m]:
                    sb = mb
                else:
                    eb = mb - 1
            while sc < ec:
                mc = (sc + ec + 1) // 2
                if food[c][mc] <= food[a][m]:
                    sc = mc
                else:
                    ec = mc - 1
            t =  m + eb + ec
            if t == k:
                print(a + 1, m)
                return 1
            elif t < k:
                s = m + 1
            else:
                e = m - 1
        return 0
    for _ in range(int(input())):
        x, y, z, k = map(int, input().split())
        if find(0, 1, 2, x, y, z, k): pass
        elif find(1, 0, 2, y, x, z, k): pass
        else: find(2, 0, 1, z, x, y, k)
solution()