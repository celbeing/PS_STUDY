# A: 가상 검증 기술
import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    ta, tb, va, vb = map(int,input().split())
    ca = ta*va
    cb = tb*vb
    if cb >= ca: print(cb)
    else:
        while cb < ca:
            ca -= ta
            cb += ta
        print(min(max(cb,ca),max(ca+ta,cb-ta)))