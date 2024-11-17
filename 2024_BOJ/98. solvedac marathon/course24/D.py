#24141: インフルエンザ(Flu)
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    m = int(input())
    d = int(input())
    k = int(input())
    sp = []
    for i in range(d + 1):
        for j in range(1, d + 1):
            if i ** 2 + j ** 2 > d ** 2:
                break
            sp += [(i, j), (i, -j), (-i, j), (-i, -j)]
    board = [[0] * 1001 for _ in range(1001)]
    for i in range(1, n + 1):
        board[]
solution()