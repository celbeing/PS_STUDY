# 16206: 롤케이크
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(key = lambda x: (x % 10, x))
    count = 0
    for cake in a:
        if m == 0: break
        if cake % 10:
            t = min(cake // 10, m)
            m -= t
            count += t
        elif cake <= (m + 1) * 10:
            t = cake // 10
            m -= t - 1
            count += t
        else:
            count += m
            m = 0
    print(count)
solution()