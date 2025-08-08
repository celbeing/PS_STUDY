# 1703: 생장점
import sys
input = sys.stdin.readline
def solution():
    while True:
        a = list(map(int, input().split()))
        if a[0] == 0: break
        res = 1
        for i in range(1, a[0] + 1):
            res *= a[i * 2 - 1]
            res -= a[i * 2]
        print(res)
solution()