# 5615: 아파트 임대
import sys
input = sys.stdin.readline

def miller_rabin(n, a):
    d = n - 1
    while d % 2 == 0:
        d >>= 1
    x = pow(a, d, n)
    if x == 1 or x == n - 1: return True
    while d != n - 1:
        x = pow(x, 2, n)
        d <<= 1
        if x == 1: return False
        elif x == n - 1: return True
    return False

def is_prime(n):
    if n in prime:
        return True
    for a in prime:
        if not miller_rabin(n, a):
            return False
    return True

prime = [2, 7, 61]

count = 0
for _ in range(int(input())):
    a = int(input()) * 2 + 1
    if is_prime(a):
        count += 1
print(count)