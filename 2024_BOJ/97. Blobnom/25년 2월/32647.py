# 32647: 골드바흐흑흙의 추측
import sys
input = sys.stdin.readline

a, b, k = map(int, input().split())
prime = []

def fast_mod_power(a, b, m):
    ret = 1
    a %= m
    while b:
        if b & 1:
            ret *= a
            ret %= m
        b >>= 1
        a **= 2
        a %= m
    return ret

def miller_rabin(n, a):
    d = n - 1
    while d & 1 == 0:
        d >>= 1
    x = fast_mod_power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = fast_mod_power(x, 2, n)
        d <<= 1
        if x == 1:
            return False
        elif x == n - 1:
            return True
    return False

def is_prime(k):
    if k in [2, 7, 61]:
        return True
    if k == 1 or k & 1 == 0:
        return False
    for t in [2, 7, 61]:
        if not miller_rabin(k, t):
            return False
    return True

for p in range(a, b + 1):
    if is_prime(p):
        prime.append(p)

conj = dict()
numbers = set()
conj[0] = 1
numbers.add(0)
for p in prime:
    new_num = set()
    for now in numbers:
        next = p + now
        if next > k: continue
        if next in conj: conj[next] += conj[now]
        else:
            conj[next] = conj[now]
            new_num.add(next)
    numbers.update(new_num)
if k in conj: print(conj[k])
else: print(0)