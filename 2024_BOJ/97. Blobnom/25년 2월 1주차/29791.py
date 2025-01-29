# 29791: 에르다 노바와 오리진 스킬
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    erda, origin = 0, 0
    t = 0
    for k in a:
        if k >= t:
            erda += 1
            t = k + 100
    t = 0
    for k in b:
        if k >= t:
            origin += 1
            t = k + 360
    print(erda, origin)
solution()