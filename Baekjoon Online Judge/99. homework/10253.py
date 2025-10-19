# 10253: 헨리
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def henry(a, b):
    f = b // a
    while 1:
        if a * f == b:
            return f
        elif a * f > b:
            a *= f
            a -= b
            b *= f
            g = gcd(a, b)
            a //= g
            b //= g
            f = b // a
        else: f += 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(henry(a, b))