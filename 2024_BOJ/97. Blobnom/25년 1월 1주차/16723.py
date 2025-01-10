# 16723: 원영이는 ZOAC과 영원하고 싶다
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    m = [2, 6]
    b = 4
    k = 2
    for _ in range(28):
        m.append(k * 2 + b * 3)
        k = k * 2 + b
        b <<= 1
    res = 0
    i = 0
    while n:
        if n & 1:
            res += m[i]
        i += 1
        n >>= 1
    print(res)
solution()