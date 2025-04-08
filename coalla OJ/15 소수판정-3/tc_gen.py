import random
random.random()
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

numbers = []
for _ in range(100000):
    numbers.append(random.randint(100_000_000_000_000, 300_000_000_000_000))

path = "C:\\Users\\kimsd\\OneDrive\\문서\\GitHub\\2024_BOJ\\coalla OJ\\15 소수판정-3\\"
file = open(path + "1.in", 'w')
w = file.writelines("100000\n")
for i in range(100000):
    w = file.writelines(f"{numbers[i]} ")
file = open(path + "1.out", 'w')
for i in range(100000):
    if is_prime(numbers[i]):
        w = file.writelines('YES\n')
    else:
        w = file.writelines('NO\n')