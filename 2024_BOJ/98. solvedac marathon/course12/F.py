#31719: UDP 스택
import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    A = deque(list(map(int,input().split())))
    U, D, P = deque([]), deque([]), deque([])
    