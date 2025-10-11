# 1619: 점 고르기
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def grad(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    dec = -1 if dx * dy < 0 else 1
    if dx < 0: dx *= -1
    if dy < 0: dy *= -1
    g = gcd(dx, dy)
    dx //= g
    dy //= g
    return tuple((dx, dy * dec))

n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]
high = 0
for i in range(n):
    grad_dict = dict()
    for j in range(n):
        if i == j: continue
        g = grad(dots[i], dots[j])
        if g in grad_dict:
            grad_dict[g].append(j)
        else:
            grad_dict[g] = [j]
    for l in grad_dict:
        high = max(high, len(grad_dict[l]) + 1)
print(high if high >= 3 else -1)