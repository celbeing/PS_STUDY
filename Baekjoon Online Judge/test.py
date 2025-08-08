import sys
input = sys.stdin.readline

def solution():
    n, x = map(int, input().split())
    a = [-int(1e9)] + list(map(int, input().split())) + [-int(1e9)]
    high = int(1e12)
    for i in range(1, n + 1):
        p, q, r = a[i - 1], a[i], a[i + 1]
        count = 0
        # 1: p < q < r
        if q - p < x:
            count += x - q + p
            if r - p - x < x:
                count += x - r + p + x
            if high > count: high = count
        else:
            if r - q < x:
                count += x - r + q
            if high > count: high = count

        count = 0
        # 2: p > q > r
        if q - r < x:
            count += x - q + r
            if p - r - x < x:
                count += x - p + r + x
            if high > count: high = count
        else:
            if p - q < x:
                count += x - p + q
            if high > count: high = count

        count = 0
        # 3: p > q < r
        if p - q < x:
            count += x - p + q
        if r - q < x:
            count += x - r + q
        if high > count: high = count

        count = 0
        # 4: p < q > r
        if q - max(p, r) < x:
            count += x - q + max(p, r)
        if high > count: high = count

    print(high)
solution()