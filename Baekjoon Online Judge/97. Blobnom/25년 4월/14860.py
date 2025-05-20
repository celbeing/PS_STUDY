# 14860: GCD 곱
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    if n > m:
        t = n
        n = m
        m = t
    res = 1
    mod = int(1e9 + 7)

    def fast_mult(n, k):
        if k == 0:
            return 1

        x = fast_mult(n, k // 2)

        if k & 1:
            return x * x * n % mod
        else:
            return x * x % mod

    sieve = [1] * (m + 1)
    prime = []
    for i in range(2, m + 1):
        if sieve[i]:
            prime.append(i)
            for j in range(i * i, m + 1, i):
                sieve[j] = 0

    for p in prime:
        c = 0
        k = p
        while k <= n:
            c += (n // k) * (m // k)
            k *= p
        res *= fast_mult(p, c)
        res %= mod
    print(res)
solution()