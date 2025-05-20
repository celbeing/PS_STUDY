#28857: Морской бой
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    s, e = 0, n + 1
    while s < e:
        m = (s + e + 1) // 2
        if m * (m + 1) * (m + 5) // 6 - 1 <= n:
            s = m
        else:
            e = m - 1
    print(e)
solution()