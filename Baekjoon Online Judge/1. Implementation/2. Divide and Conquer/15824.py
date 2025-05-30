# 15824: 너 봄에는 캡사이신이 맛있단다
import sys
input = sys.stdin.readline
mod = 10**9 + 7

def power(n, k):
    ret = 1
    while k:
        if k & 1:
            ret *= n
            ret %= mod
        n **= 2
        n %= mod
        k >>= 1
    return ret

def solution():
    n = int(input())
    scoville = sorted(list(map(int, input().split())))

    res = 0
    for i in range(n):
        res += ((power(2, i) % mod - power(2, n - i - 1) % mod) * scoville[i]) % mod
        res %= mod
    print(res)

solution()