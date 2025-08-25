n = 16
now = [0] * n

def Count(i, j, now):
    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    ret = 0
    for di, dj in d:
        x, y = i + di, j + dj
        if 0 <= x < n and 0 <= y < n:
            if now[x] & 1 << y: ret += 1
    return ret

def gen(now):
    next = [0] * n
    for i in range(n):
        for j in range(n):
            c = Count(i, j, now)
            if now[i] & 1 << j and c in (2, 3):
                next[i] |= 1 << j
            elif now[i] & 1 <<j == 0 and c == 3:
                next[i] |= 1 << j
    for i in range(n):
        now[i] = next[i]

def solution(i):
    now = i[:]

    count = 0
    check = dict()
    check[tuple(now)] = 0
    while True:
        count += 1
        gen(now)
        k = tuple(now)
        if k in check:
            return (count, count - check[k])
        else:
            check[k] = count

