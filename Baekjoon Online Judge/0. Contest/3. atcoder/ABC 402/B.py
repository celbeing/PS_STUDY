import sys
from collections import deque
input = sys.stdin.readline
def solution():
    dq = deque()
    for _ in range(int(input())):
        q = list(map(int, input().split()))
        if q[0] == 1:
            dq.append(q[1])
        else:
            print(dq.popleft())
solution()