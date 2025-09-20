# 11414: LCM
import sys
input = sys.stdin.readline

def euc(a, b):
    while b:
        a, b = b, a % b
    return a

def solution():
    a, b = map(int, input().split())
    if a == b:
        print(1)
        return

    if a > b: a, b = b, a
    factors = []
    for i in range(1, int((b - a) ** 0.5) + 1):
        if (b - a) % i == 0:
            factors.append(i)
            factors.append((b - a) // i)

    res = 1
    lcm = (a + 1) * (b + 1) // euc(a + 1, b + 1)
    for f in factors:
        rem = a % f
        n = f - rem
        l = (a + n) * (b + n) // f
        if lcm > l:
            lcm = l
            res = n
        elif lcm == l and res > n:
            res = n
    print(res)

solution()