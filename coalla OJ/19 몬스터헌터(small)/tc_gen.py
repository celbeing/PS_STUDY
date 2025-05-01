path = "C:\\Users\\kimsd\\OneDrive\\문서\\GitHub\\2024_BOJ\\coalla OJ\\19 몬스터헌터(small)\\"
file_no = 1
while True:
    file = open(path + f"{file_no}.in", 'w')
    h, n, m = map(int, input().split())
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