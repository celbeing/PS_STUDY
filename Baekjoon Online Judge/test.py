def rev(k):
    ret = 0
    while k:
        ret *= 10
        ret += k % 10
        k //= 10
    return ret

x, y = map(int, input().split())
print(rev(rev(x) + rev(y)))