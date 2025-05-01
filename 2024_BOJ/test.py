h, d, s = map(int, input().split())
a, b = 0, 0
while h > 0:
    sa = (h * s) // 100
    if sa > d:
        b += 1
        h -= sa
    else:
        a += 1
        h -= d
print(a, b)