import random, math
random.random()

path = "C:\\Users\\kimsd\\OneDrive\\문서\\GitHub\\2024_BOJ\\coalla OJ\\20 몬스터헌터(large)\\"

def fast_exp(n, k):
    ret = 1
    while k:
        if k & 1:
            ret *= n
        n **= 2
        k >>= 1
    return ret

def sleep_damage(hp, count, p):
    ret = hp * fast_exp(p, count - 1)
    ret -= hp * fast_exp(p, count)
    return ret

for file_no in range(51, 61):
    file = open(path + f"{file_no}.in", 'w')
    h, d, s = map(int, input().split())
    '''h = random.randint(1, 1_000_000_000)
    d = random.randint(1, h)
    s = random.randint(1, 100)'''
    w = file.writelines(f'{h} {d} {s}')

    a, b = 0, 0
    p = (100 - s) / 100
    i, j = 0, 3000
    while i < j:
        m = (i + j + 1) // 2
        k = sleep_damage(h, m, p)
        if k > d:
            i = m
        else:
            j = m - 1
    b = i
    h *= fast_exp(p, b)
    a = math.ceil(h / d)
    file = open(path + f"{file_no}.out", 'w')
    w = file.writelines(f'{a} {b}')
    file_no += 1