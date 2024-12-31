# 18235: 지금 만나러 갑니다
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, a, b = map(int, input().split())
    if a > b:
        k = a
        a = b
        b = k
    if b - a & 1:
        print(-1)
        return
    step = (b - a) >> 1
    res = step.bit_length()
    duck = deque([(a, b)])
    d = 1
    while step:
        t = len(duck)
        if step & 1:
            for i in range(t):
                a, b = duck.popleft()
                duck.append((a + d, b - d))
        else:
            for i in range(t):
                a, b = duck.popleft()
                if a + d <= n and b + d <= n:
                    duck.append((a + d, b + d))
                if a > d and b > d:
                    duck.append((a - d, b - d))
        step >>= 1
        d <<= 1
    if duck: print(res)
    else: print(-1)
solution()