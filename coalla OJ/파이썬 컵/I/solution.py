cand = dict()
high = 0
res = 0
for _ in range(100000):
    n = int(input())
    if n in cand:
        cand[n] += 1
    else:
        cand[n] = 1
    if high < cand[n]:
        high = cand[n]
        res = n
print(f'{res}\n{high}')