mod = int(1e9 + 7)

def fast_power(n, k):
    ret = 1
    while k:
        if k & 1:
            ret *= n
            ret %= mod
        n **= 2
        n %= mod
        k //= 2
    return ret

n, k = map(int, input().split())
print(fast_power(n, k))