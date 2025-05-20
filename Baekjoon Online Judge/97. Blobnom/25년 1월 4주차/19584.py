# 19584: 난개발
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    spot = dict()
    cor_y = set()

    for i in range(1, n + 1):
        x, y = map(int, input().split())
        spot[i] = y
        cor_y.add(y)
    cor = sorted(list(cor_y))
    comp = dict()
    for i in range(len(cor)):
        comp[cor[i]] = i

    road = [0] * len(cor)
    end = [0] * len(cor)
    for _ in range(m):
        u, v, c = map(int, input().split())
        u = comp[spot[u]]
        v = comp[spot[v]]
        if u < v:
            road[u] += c
            end[v] += c
        else:
            end[u] += c
            road[v] += c

    res = road[0]
    for i in range(1, len(cor)):
        road[i] += road[i - 1]
        if res < road[i]:
            res = road[i]
        road[i] -= end[i]
    print(res)
solution()