# 과녁 맞히기
import sys
input = sys.stdin.readline
def solution():
    mod = int(1e9 + 7)
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    def fact(n):
        ret = 1
        for i in range(2, n + 1):
            ret *= i
            ret %= mod
        return ret

    def fast_power(n, k):
        ret = 1
        while k:
            if k & 1:
                ret *= n
                ret %= mod
            n **= 2
            n %= mod
            k //= 2
        return ret

    res = fact(n)
    den = 1
    dou = 0
    for i in a:
        den *= fact(i)
        den %= mod
        if i > 1:
            dou += i - 1
    res *= fast_power(den, mod - 2)
    res %= mod

    res *= fast_power(2, dou)
    res %= mod

    print(res)
solution()