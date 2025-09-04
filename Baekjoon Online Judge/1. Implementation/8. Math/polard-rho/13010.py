import sys
input = sys.stdin.readline
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def fast_mod_power(x, y, mod):
    ret = 1
    x %= mod
    while y:
        if y & 1:
            ret *= x
            ret %= mod
        y >>= 1
        x **= 2
        x %= mod
    return ret

def miller_rabin(n, a):
    d = n - 1
    while d % 2 == 0:
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

def is_prime(n):
    if n in prime:
        return True
    if n == 1 or n & 1 == 0:
        return False
    for a in prime:
        if not miller_rabin(n, a):
            return False
    return True

def euc(a, b):
    while b:
        a, b = b, a % b
    return a

def polard_rho(n, x):
    k = x
    if is_prime(n):
        return n

    for p in prime:
        if n % p == 0:
            return p

    y = x
    d = 1
    while d == 1:
        x = ((x * x) + 1) % n
        y = ((y * y) + 1) % n
        y = ((y * y) + 1) % n
        d = euc(abs(x - y), n)
    if d == n:
        return polard_rho(n, k + 1)
    else:
        if is_prime(d):
            return d
        else:
            return polard_rho(d, 2)

n = int(input())
factor = dict()
while n != 1:
    f = polard_rho(n, 2)
    if f in factor: factor[f] += 1
    else: factor[f] = 1
    n //= f

gcd_of_exp = 0
for f in factor:
    if gcd_of_exp:
        gcd_of_exp = euc(gcd_of_exp, factor[f])
    else:
        gcd_of_exp = factor[f]

factor_exp = []
for i in range(gcd_of_exp, 0, -1):
    if gcd_of_exp % i == 0: factor_exp.append(i)

for fe in factor_exp:
    count = 1
    for f in factor:
        count *= (factor[f] // fe) + 1
    if count == fe:
        res = 1
        for f in factor:
            res *= f ** (factor[f] // fe)
        print(res)
        break
else: print(-1)