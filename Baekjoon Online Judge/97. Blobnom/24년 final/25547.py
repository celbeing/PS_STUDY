# 25547: 신기한 숫자
import sys
input = sys.stdin.readline
def solution():
    a, b = map(int, input().split())
    if b % a:
        print(0)
    else:
        b //= a
        res = 0
        for i in range(1, int(b ** 0.5) + 1):
            if b % i == 0: res += 2
        if int(b ** 0.5) ** 2 == b: res -= 1
        print(res)
solution()