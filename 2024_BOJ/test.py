import sys

h, d, s = map(int, input().split())
sys.setrecursionlimit()
def fast_exp(n, k):
    ret = 1
    while k:
        if k & 1:
            ret *= n
        n **= 2
        k >>= 1
    return ret

i = 0
t = h
p = (100 - s) / 100
while t >= 1:
    t *= p
    i += 1
print(f'{i}번째 예상 = {h * fast_exp(p, i)}')

i, j = 0, 3000
while i < j:
    m = (i + j) // 2
    k = h * fast_exp(p, m)
    if k * p > d:
        i = m + 1
    else:
        j = m
print(f'예상 수면참 횟수: {i}회')

count = 1
s /= 100
while h > d:
    h -= h * s
    print(f'공격 {count}회차 체력: {h}')
    count += 1