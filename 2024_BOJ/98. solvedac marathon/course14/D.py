#28127: 숫자탑과 쿼리
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        a, d, x = map(int, input().split())
        l, r = 1, 1414
        while l < r:
            m = (l + r) // 2
            if a * m + d * m * (m - 1) // 2 < x:
                l = m + 1
            else: r = m
        print(r, x - (a * (r - 1) + d * (r - 1) * (r - 2) // 2))
solution()