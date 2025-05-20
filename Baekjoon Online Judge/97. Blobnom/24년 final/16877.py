# 16877: 핌버
import sys
input = sys.stdin.readline
def solution():
    fib = [1] * 32
    grundy = [0] * 3000001
    for i in range(2, 32):
        fib[i] = fib[i - 1] + fib[i - 2]
    for i in range(1, 3000001):
        states = [0] * 16
        for f in fib:
            if f > i: break
            states[grundy[i - f]] = 1
        for g in range(16):
            if states[g] == 0:
                grundy[i] = g
                break

    n = int(input())
    p = list(map(int, input().split()))
    res = grundy[p[0]]
    for i in range(1, n):
        res ^= grundy[p[i]]
    print("koosaga" if res else "cubelover")
solution()