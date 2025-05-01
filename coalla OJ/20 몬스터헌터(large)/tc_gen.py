import random
random.random()

path = "C:\\Users\\kimsd\\Documents\\GitHub\\2024_BOJ\\coalla OJ\\20 몬스터헌터(large)\\"
for file_no in range(1, 51):
    file = open(path + f"{file_no}.in", 'w')
    h = random.randint(1,1000000000)
    w = file.writelines(f'{h} {n} {m}')
    a, b = 0, 0
    while h > 0:
        if ((h * m) // 100) > n:
            b += 1
            h -= (h * m) // 100
        else:
            a += 1
            h -= n
    file = open(path + f"{file_no}.out", 'w')
    w = file.writelines(f'{a} {b}')
    file_no += 1