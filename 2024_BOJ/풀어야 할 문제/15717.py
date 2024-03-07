#15717: 떡파이어
N = int(input())
div = int(1e9+7)
def power(C,n):
    if n < 1:
        return 1
    r = 1
    while n:
        if n & 1:
            r *= C
            r %= div
        C *= C
        C %= div
        n = n >> 1
    return r

print(power(2,N-1))