#4276: 0이 몇 개?
import sys
input = sys.stdin.readline
def count_zero(n):
    if n < 0: return 0
    ret = 1
    k = n
    d = 1
    while d * 10 <= n:
        ret += (k // 10) * d
        if k % 10 == 0 and d > 1:
            ret -= d - n % d - 1
        k //= 10
        d *= 10
    return ret

while True:
    a, b = map(int, input().split())
    if a < 0 and b < 0: break

    print(count_zero(b) - count_zero(a - 1))