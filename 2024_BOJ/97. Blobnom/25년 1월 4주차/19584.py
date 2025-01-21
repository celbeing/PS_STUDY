# 19584: 난개발
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    spot = [[0,0,0]] + [list(map(int, input().split())) + [i] for i in range(1, n + 1)]
    spot.sort(key = lambda x: x[1])
solution()