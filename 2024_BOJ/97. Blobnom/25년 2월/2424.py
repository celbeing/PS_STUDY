# 2424: 부산의 해적
import sys
input = sys.stdin.readline
def solution():
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n, m = map(int, input().split())
    treasure_map = [list(input().rstrip()) for _ in range(n)]
    