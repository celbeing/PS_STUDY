import sys
input = sys.stdin.readline
for _ in range(int(input())):
    code = int(input())
    sic = {}
    c = 2
    while c**2 <= code:
        while code % c == 0:
            if not c in sic: sic[c] = 0
            sic[c] += 1
            code /= c
        c += 1
    if code > 1: sic[code] = 1

    r = []
    for fac in sic:
        n = sic[fac]
        c = fac
        while n > 0:
            if n&1: r.append(int(c))
            n >>= 1
            c *= c
    r.sort()
    print(*r)