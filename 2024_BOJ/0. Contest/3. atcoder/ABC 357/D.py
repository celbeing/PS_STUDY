n = input()
dig = len(n)
n = int(n)
m = 998244353

if n < m:
    p = 0
    for i in range(n):
        p *= 10**dig
        p += n
        p %= m
    print(p)