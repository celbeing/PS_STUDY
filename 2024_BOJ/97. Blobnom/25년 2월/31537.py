# 31537: 출근하기 싫어 1
import sys
input = sys.stdin.readline
def solution():
    mod = int(1e9 + 7)
    factorial = [1] * 1000001
    inv_factorial = [1] * 1000001
    for i in range(2, 1000001):
        factorial[i] = (factorial[i - 1] * i) % mod

    def fast_power(n, p):
        result = 1
        while p:
            if p & 1:
                result *= n
                result %= mod
            n **= 2
            n %= mod
            p >>= 1
        return result

    def combination(m, p):
        result = factorial[m]
        k = (factorial[p] * factorial[m - p]) % mod
        result *= fast_power(k, mod - 2)
        result %= mod
        return result

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    lack = 0
    res = 1
    for k in a:
        if k < lack:
            res = 0
            break
        p = k - lack
        res *= combination(m, p)
        t = m - p
        m -= t
        lack += t
        res %= mod
    print(res)
solution()