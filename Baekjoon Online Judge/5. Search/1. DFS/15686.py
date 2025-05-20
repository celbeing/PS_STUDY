# 15686: 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    inf = int(1e9)
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    home = []
    dark = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                home.append((i, j))
            elif city[i][j] == 2:
                dark.append((i, j))
    h, d = len(home), len(dark)
    dist = [[inf] * d for _ in range(h)]
    for i in range(h):
        for j in range(d):
            dist[i][j] = abs(home[i][0] - dark[j][0]) + abs(home[i][1] - dark[j][1])

    def check(c):
        ret = 0
        for i in range(h):
            near = inf
            for j in c:
                near = min(near, dist[i][j])
            ret += near
        return ret

    res = inf
    chicken_zip = [i for i in range(d)]
    comb = combinations(chicken_zip, m)
    for c in comb:
        res = min(res, check(c))
    print(res)
solution()