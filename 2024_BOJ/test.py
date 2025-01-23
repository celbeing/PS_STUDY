import sys
from collections import deque
input = sys.stdin.readline
def solution():
    t = []
    mod = 20200429

    for i in range(48, 58): t.append(i)
    for i in range(65, 91): t.append(i)
    for i in range(97,123): t.append(i)
    for i in range(62):
        k = t[i]
        for j in range(813):
            t[i] *= k
            t[i] %= mod
    print((t[2]+t[29]+t[32]+t[44]+t[50]) % mod)
solution()