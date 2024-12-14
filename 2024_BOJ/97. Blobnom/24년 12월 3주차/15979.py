# 15979: 스승님 찾기
import sys
input = sys.stdin.readline
def solution():
    m, n = map(int, input().split())
    m = abs(m)
    n = abs(n)
    if m == n == 0:
        print(0)
        return 0
    while n > 0:
        m, n = n, m % n
    print(1 if m == 1 else 2)
solution()