# 20165: 인내의 도미노 장인 호석
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m, r = map(int, input().split())
    d = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    board = [list(map(int, input().split())) for _ in range(n)]
    check = [['S'] * m for _ in range(n)]
    for _ in range(r):
        x, y, d = map(str, input().split())
        x = int(x) - 1; y = int(y) - 1
        
        x, y = map(int, input().split())
        check[x - 1][y - 1] = 'S'
