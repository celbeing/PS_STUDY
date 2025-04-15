# 32689: 트랙 정리하기
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    a = deque(list(map(int, input().split())))
    a.popleft()
    f, b = deque([0]), deque([0])
    fw, bw = 0, 0
    res = 0
    while a:
        if fw <= bw:
            f.append(a.popleft())
            fw += f[-1]
        else:
            b.append(a.pop())
            bw += b[-1]
    if fw > bw:
        t = (fw - bw) // 2
        f[-1] -= t
        fw -= t
        bw += t
        b.append(t)
    else:
        t = (bw - fw + 1) // 2
        b[-1] -= t
        fw += t
        bw -= t
        f.append(t)
    for i in range(len(f)):
        res += f[i] * i
    for i in range(len(b)):
        res += b[i] * i
    res *= 2
    if fw > bw:
        res -= len(f)
    else:
        res -= len(b)
    print(res + 1)
solution()