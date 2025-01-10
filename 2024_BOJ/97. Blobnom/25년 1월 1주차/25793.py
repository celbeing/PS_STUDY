# 25793: 초콜릿 피라미드
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        r, c = map(int, input().split())
        if r < c: r, c = c, r
        t = (c * (c + 1) * (c * 2 + 1)) // 6
        d = (c * (c + 1)) // 2
        k = r - c
        res = t * 2 + (k - 1) * d * 2 - k * c
        print(res + c, res)
solution()