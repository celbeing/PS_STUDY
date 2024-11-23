# 16197: 두 동전
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    