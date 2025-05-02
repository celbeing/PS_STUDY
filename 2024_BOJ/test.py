import sys, math
input = sys.stdin.readline
h, d, s = map(int, input().split())
def fast_exp(n, k):
    ret = 1
    while k:
        if k & 1:
            ret *= n
        n **= 2
        k >>= 1
    return ret

def sleep_damage(hp, count, p):
    ret = hp * fast_exp(p, count - 1)
    ret -= hp * fast_exp(p, count)
    return ret

p = (100 - s) / 100
i, j = 0, 3000
while i < j:
    m = (i + j + 1) // 2
    k = sleep_damage(h, m, p)
    if k > d:
        i = m
    else:
        j = m - 1
h *= fast_exp(p, i)
j = math.ceil(h / d)
print(j, i)