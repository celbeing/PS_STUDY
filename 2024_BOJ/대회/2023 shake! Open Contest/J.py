#J: 볼록볼록
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
peek = -1
dot = deque()
for _ in range(1,N):
    while dot:
        