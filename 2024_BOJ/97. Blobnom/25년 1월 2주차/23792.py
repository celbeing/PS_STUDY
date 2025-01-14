# 23792: K번째 음식 찾기 2
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    food = [[0] + list(map(int, input().split())) for _ in range(2)]
    def find(a, b, x, y, k):
        s, e = 0, x
        while s <= e:
            m = (s + e) // 2
            sb,eb, = 0, y
            while sb < eb:
                mb = (sb + eb + 1) // 2
                if food[b][mb] <= food[a][m]:
                    sb = mb
                else:
                    eb = mb - 1
            t =  m + eb
            if t == k:
                print(a + 1, m)
                return 1
            elif t < k:
                s = m + 1
            else:
                e = m - 1
        return 0
    for _ in range(int(input())):
        x, y, k = map(int, input().split())
        if find(0, 1, x, y, k): pass
        else: find(1, 0, y, x, k)
solution()