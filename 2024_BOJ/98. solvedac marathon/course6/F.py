def check(k):
    rem = 1
    res = 1
    t = 10
    while k>rem>0:
        rem += t
        t *= 10
        t %= k
        rem %= k
        res += 1
    return res

N = int(input())
if N & 1 and N % 10 != 5:
    print(check(N))
else:
    print(-1)