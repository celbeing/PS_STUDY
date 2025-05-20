# 31221: 어려운 정수 맞히기 게임
import sys
from math import ceil, floor
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        a, b = 0, 0
        l, r = 0, int(1e18)
        while r - l > 4:
            a = l
            b = floor((l + r) // 2)
            print("?", a, b)
            sys.stdout.flush()
            result = input().rstrip()
            if result == '+':
                l += b ** 2
            elif result == '-':
                r = l + b ** 2
            else:
                l += b ** 2
                break
        while True:
            print("?", l, 1)
            sys.stdout.flush()
            result = input().rstrip()
            if result == '+':
                l += 1
            elif result == '0':
                l += 1
                break
        print("!", l)
        sys.stdout.flush()
solution()