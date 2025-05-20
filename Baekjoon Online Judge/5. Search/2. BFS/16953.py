# 16953: A -> B
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    a, b = map(int, input().split())
    dq = deque([(1, a)])
    while dq:
        c, now = dq.popleft()
        if now == b:
            return c

        if (now << 1) <= b:
            dq.append((c + 1, now << 1))

        if (now * 10) + 1 <= b:
            dq.append((c + 1, (now * 10) + 1))
    return -1
print(solution())