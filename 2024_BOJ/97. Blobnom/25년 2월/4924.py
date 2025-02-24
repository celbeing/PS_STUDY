# 4924: 정수론 싫어
import sys
input = sys.stdin.readline
def solution():
    sieve = [0] * 1000001
    for i in range(2, 1000001):
        if sieve[i]: continue
        else:
            k = i
            while k < 1000001:
                for j in range(k, 1000001, k):
                    sieve[j] += 1
                k *= i
            sieve[i] = -1
    for i in range(1, 1000001):
        sieve[i] += sieve[i - 1]
    t = 1
    while True:
        l, u = map(int, input().split())
        if l < 0: break

    print()
solution()