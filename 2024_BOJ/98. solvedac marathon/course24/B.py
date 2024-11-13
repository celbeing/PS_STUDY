#2685: 님비합
import sys
input = sys.stdin.readline

def base_k(k, n):
    ret = []
    while n:
        ret.append(n % k)
        n //= k
    return ret

def oct(k, n):
    ret = 0
    while n:
        ret *= k
        ret += n.pop()
    return ret

def solution():
    for _ in range(int(input())):
        b, x, y = map(int, input().split())
        x = base_k(b, x)
        y = base_k(b, y)
        if len(x) > len(y):
            for i in range(len(y)):
                x[i] += y[i]
                x[i] %= b
            print(oct(b, x))
        else:
            for i in range(len(x)):
                y[i] += x[i]
                y[i] %= b
            print(oct(b, y))

solution()