# 17466: N! mod P (1)
import sys
input = sys.stdin.readline

def solution():
    N, P = map(int, input().split())
    if N > P // 3:
        product = 1
        for i in range(N + 1, P):
            product = (product * i) % P
        k = -pow(product, P - 2, P)
        print(k % P)
    else:
        k = 1
        for i in range(2, N + 1):
            k *= i
            k %= P
        print(k)
solution()