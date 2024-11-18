# 15563: Äventyr 1
# centroid decomposition을 배워보자
import sys
input = sys.stdin.readline

def solution():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    violin = set()
    for _ in range(Q):
        c, v = map(int, input().split())
        if c == 1:
            violin.add(v)
        else:
            axis = sorted(list(violin))
            l, r = 0, N + 1
            s, e = 0, len(axis)
            while s < e:
                m = (s + e) // 2
                if axis[m] < v:
                    s = m + 1
                else:
                    e = m
                if e < len(axis):
                    r = axis[e]
                if s > 0:
                    l = axis[s - 1]
            if l == 0 and r == N + 1:
                print(-1)
            elif l == 0:
                print(r - v)
            elif r == N + 1:
                print(v - l)
            else:
                print(min(r - v, v - l))
solution()