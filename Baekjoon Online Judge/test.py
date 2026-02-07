k = int(input())
a = int(input())
small = large = a

t = 10 ** (k - 1)
for _ in range(k - 1):
    tmp = a // t
    a %= t
    a *= 10
    a += tmp
    if a > large:
        large = a
    elif a < small:
        small = a

print(large - small)