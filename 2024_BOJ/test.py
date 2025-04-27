
r = int(input())
res = r
while r > 1:
    if r & 1:
        r *= 3
        r += 1
    else:
        r //= 2
    res = max(r, res)
print(res)