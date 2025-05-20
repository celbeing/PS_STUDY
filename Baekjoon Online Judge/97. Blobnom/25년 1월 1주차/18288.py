# 18288: 팀 연습
import sys
input = sys.stdin.readline
def solution():
    mod = int(1e9 + 7)
    n, k = map(int, input().split())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    da = [0] * (n + 1)
    db = [0] * (n + 1)
    if k == 1:
        a[1] = 1
        da[1] = 1
    b[1] = 1
    db[1] = 1
    c[1] = 1
    for i in range(2, n + 1):
        if k and i % k == 0:
            a[i] = a[i - 1] + b[i - 1] + c[i - 1]
            da[i] = da[i - 1] + db[i - 1]
            a[i] %= mod
            da[i] %= mod
        b[i] = a[i - 1] + c[i - 1]
        db[i] = da[i - 1]
        db[i] %= mod
        b[i] %= mod
        c[i] = a[i - 1] + b[i - 1] + c[i - 1]
        c[i] %= mod
    res = a[n] + b[n] + c[n] - da[n] - db[n]
    print(res % mod)
solution()