# 8583: Skracalne liczby pierwsze
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def fast_mod_power(x, y, mod):
        ret = 1
        x %= mod
        while y:
            if y & 1:
                ret *= x
                ret %= mod
            y >>= 1
            x **= 2
            x %= mod
        return ret

    def miller_rabin(n, a):
        d = n - 1
        while d & 1 == 0:
            d >>= 1
        x = fast_mod_power(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = fast_mod_power(x, 2, n)
            d <<= 1
            if x == 1:
                return False
            elif x == n - 1:
                return True
        return False

    def is_prime(n):
        if n in prime:
            return True
        if n == 1 or n & 1 == 0:
            return False
        for a in prime:
            if not miller_rabin(n, a):
                return False
        return True

    a, b = map(int, input().split())
    reducible_prime = deque([2, 3, 5, 7])
    result = 0
    while reducible_prime:
        k = reducible_prime.popleft()
        if k > b: break
        if a <= k <= b: result += 1
        k *= 10
        for i in range(1, 10, 2):
            if is_prime(k + i):
                reducible_prime.append(k + i)
    print(result)
solution()